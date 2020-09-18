# Folding@home Page Renderer

This application takes the translations from [FoldingCommunity/Translate](https://github.com/FoldingCommunity/Translate)
and injects them into templates to render out HTML pages for all the languages we are supporting.

It is part of a larger system (currently in construction), which will semi-automate the updating of the
[Folding@home website](https://foldingathome.org).

## Usage

1. Make sure you initialized and updated the submodules
       
       $ git submodule init
       $ git submodule update
       
   This will make sure that you have the latest version of all the translations and templates.
   
2. Just run the rendering script and it will dump the rendered pages into `output/`:

       $ python3 render.py

## Next Steps

This application is currently in a very early stage. There are lots of things to improve:

**Check out the [open issues](https://github.com/FoldingCommunity/PageRenderer/issues) to find out more.**