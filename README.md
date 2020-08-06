# Folding @ home Page Renderer

This application takes the translations from [FoldingCommunity/Translate](https://github.com/FoldingCommunity/Translate)
and injects them into templates to render out HTML pages for all the languages we are supporting.

It is part of a larger system (currently in construction), which will semi-automate the updating of the
[Folding @ home website](https://foldingathome.org).

## Usage

1. Make sure you initialized and updated the submodules
       
       $ git submodules init
       $ git submodules update
       
   This will make sure that you have the latest version of all the translations.
   
2. Just run the rendering script and it will dump the rendered pages into `output/`:

       $ python3 render.py

## Next Steps

This application is currently in a very early stage. There are lots of things to improve:

- [ ] Replace custom Markdown parser with something more solid
- [ ] Replace fake Mustache renderer with an actual implementation or use something else
- [ ] Create actual templates for all the pages to be rendered
- [ ] Extract the templates from this repository into a dedicated one (and maybe link it in here as submodule)
- [ ] Integration with the component that pushes the pages into Wordpress