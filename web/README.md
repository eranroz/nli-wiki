# How to run me
Install requirements from nli_app

```
pip3 install -r nli_app/requirements.txt
```
Run:
```
flask --app nli_app
```

# TODOs
* Web interface prototype - design UI for this tool (nli-wiki on toolslab)
* Provide access to commons [(OAuth)](https://www.mediawiki.org/wiki/Help:OAuth) - for upload
* Access to NLI collections  - we will focus [Dan Hadani collection](http://web.nli.org.il/sites/NLI/Hebrew/Documents/DANHADANI.pdf)
 * Extract metadata
 * Data have rich description
 * but it is mostly in English - we should provide wikidata/commons annotation for intelanguage access
 * Copyrights seems to be OK (need double check before upload to commons!)
* Enriching the context based on Wiki or wikidata (term finding/linking/category suggestion)