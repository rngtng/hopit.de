# hopit.de

Latest version of http://hopit.de + static archive from 2009-2019.

## Serve docs locally

The site uses MkDocs Material plus extra plugins (`mkdocs-video`, `git-revision-date-localized`, ...) that are not in the stock image, so build the custom image once:

```bash
docker build -t hopit-docs .
```

Then serve with live reload at <http://localhost:24001>:

```bash
docker run --rm -it -p 24001:24001 -v ${PWD}:/docs hopit-docs serve -a 0.0.0.0:24001
```

Plugins are defined in [requirements.txt](requirements.txt); rebuild the image after changing it.
