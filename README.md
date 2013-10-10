markdown-icons (iconfonts.py)
==============

Easily display icon fonts in markdown. Just add the css necessary for your font and add this extension.

Although I made this to work with any icon font, I have added a `mod` syntax to add more prefixed classes to support [Font Awesome](http://fortawesome.github.io/Font-Awesome/) and its special classes such as `2x, 3x, muted, spin, etc`

- You can create your own Icon Fonts using the IcoMoon app: http://icomoon.io/app/
- A great pre-made Icon Font is [Font Awesome (GitHub Project)](http://fortawesome.github.io/Font-Awesome/)

Use it in any personal or commercial project you want.

Syntax:
========

- Accepts a-z, A-Z, 0-9, _(underscore), and - (hypen)
- Uses [HTML Entity](http://www.w3schools.com/html/html_entities.asp) like syntax: `&entity_name;`

```
&icon-html5;
&icon-css3;
&icon-my-icon;

&icon-html5:2x;
&icon-quote:3x,muted;
&icon-spinner:large,spin;
```

#### Example Markdown:

```
I love &icon-html5; and &icon-css3;
&icon-spinner:large,spin; Sorry we have to load...
```

##### Output:

```
I love <i aria-hidden="true" class="icon-html5"></i> and <i aria-hidden="true" class="icon-css3"></i>
<i aria-hidden="true" class="icon-spinner icon-large icon-spin"></i> Sorry we have to load...
```

Installation:
==============
Just drop it in the extensions folder of the markdown package: `markdown/extensions`


Usage / Setup:
==============
#### Default Prefix is "icon-":
##### In a Django Template: 
`{{ textmd|markdown:"safe,iconfonts" }}`

##### In Python:
```
md = markdown.Markdown(extensions=['iconfonts'])
converted_text = md.convert(text)
```


#### Use a custom Prefix:
##### In a Django Template:
`{{ textmd|markdown:"safe,iconfonts(prefix=mypref-)" }}`

##### In Python:
```
md = markdown.Markdown(extensions=['iconfonts(prefix=mypref-)'])
converted_text = md.convert(text)
```

#### No prefix (just in case you couldn't figure it out :P):
This isn't suggested, as it will take over the already built in HTML Entities
##### In a Django Template:
`{{ textmd|markdown:"safe,iconfonts(prefix=)" }}`

##### In Python:
```
md = markdown.Markdown(extensions=['iconfonts(prefix=)'])
converted_text = md.convert(text)
```
