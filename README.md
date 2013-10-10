markdown-icons (iconfonts.py)
==============

Easily display icon fonts in markdown. Just add the css necessary for your font and add this extension.

Although I made this to work with any icon font, I have added a `mod` syntax to add more prefixed classes to support [Font Awesome](http://fortawesome.github.io/Font-Awesome/) and its special classes such as `2x, 3x, muted, spin, etc`

- You can create your own Icon Fonts using the IcoMoon app: http://icomoon.io/app/
- A great pre-made Icon Font is [Font Awesome (GitHub Project)](http://fortawesome.github.io/Font-Awesome/)

Syntax:
========

- Accepts a-z, A-Z, 0-9, and - (hypen)
- Uses [HTML Entity](http://www.w3schools.com/html/html_entities.asp) like syntax: `&entity_name;`

```
&icon-html5;
&icon-css3;
&icon-my-icon;

&icon-html5:2x;
&icon-quote:3x,muted;
&icon-spinner:large,spin;
```
