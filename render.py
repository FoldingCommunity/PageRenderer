from pathlib import Path
import re
from babel._compat import StringIO
from babel.messages.pofile import read_po


# TODO This should probably be replaced with something more reasonable
def _convert_markdown(message: str) -> str:
    message = re.sub('\\*\\*((?!\\*\\*).)*\\*\\*', '<strong>\\1</strong>', message)
    message = re.sub('\\[([^]]+)]\\(([^)]+)\\)', '<a href="\\2">\\1</a>', message)
    return message


# TODO This could be improved (I tried to use chevron, but it doesn't deal well with dots in keys)
def _render_page(template: str, messages: dict):
    output = template
    for (key, message) in messages.items():
        output = output.replace('{{{ ' + key + ' }}}', message)
    return output


def render_pages(translations_path: Path, template_path: Path, output_path: Path):
    if not output_path.exists():
        output_path.mkdir()
    translations = {}
    for directory in translations_path.glob('??-??'):
        if directory.is_dir() and directory.stem != 'en-US':
            translations[directory.stem] = directory
    for template in template_path.glob('*.php'):
        print(f'Rendering {template}')
        with template.open('r', encoding='UTF-8') as tpl_file:
            raw_template = tpl_file.read()
            for (translation, path) in translations.items():
                print(f'\tProcessing {translation}...')
                try:
                    translation_file = translations_path / translation / (template.stem + '.po')
                    if not translation_file.exists():
                        print(
                            f'\t\tTranslation of file {template.name} for language {translation} is missing: {translation_file}')
                        continue
                    with translation_file.open('r', encoding='UTF-8') as lang_file:
                        raw_messages = read_po(StringIO(lang_file.read()), charset='UTF-8')
                        messages = {}
                        for message in raw_messages:
                            messages[message.id] = _convert_markdown(message.string)
                        print(messages)
                        output = _render_page(raw_template, messages)
                        output_file = output_path / translation / template.name
                        if not output_file.parent.exists():
                            output_file.parent.mkdir()
                        with open(output_path / translation / template.name, 'w', encoding='UTF-8') as out_file:
                            out_file.write(output)
                except Exception as e:
                    print(f'\tERROR: {e}')


if __name__ == '__main__':
    render_pages(
        translations_path = Path('translations/Localization/'),
        template_path = Path('templates/'),
        output_path = Path('output/')
    )

