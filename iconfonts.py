"""
IconFonts Extension for Python-Markdown
========================================

Description:
	Use this extension to display icon font icons in markdown. Just add the css necessary for your font and add this extension.

	Although I made this to work with any icon font, I have added a "mod" syntax to 
	add more prefixed classes to support [Font Awesome](http://fortawesome.github.io/Font-Awesome/) and its special classes

	- You can create your own Icon Fonts using the IcoMoon app: http://icomoon.io/app/
	- A great pre-made Icon Font is [Font Awesome (GitHub Project)](http://fortawesome.github.io/Font-Awesome/)

Syntax:
	- Accepts a-z, A-Z, 0-9, _ (underscore), and - (hypen)
	- Uses HTML Entity like syntax

	&icon-html5;
	&icon-css3;
	&icon-my-icon;

	&icon-html5:2x;
	&icon-quote:3x,muted;
	&icon-spinner:large,spin;


Example Markdown:
	I love &icon-html5; and &icon-css3;
	&icon-spinner:large,spin; Sorry we have to load...
Output:
	I love <i aria-hidden="true" class="icon-html5"></i> and <i aria-hidden="true" class="icon-css3"></i>
	<i aria-hidden="true" class="icon-spinner icon-large icon-spin"></i> Sorry we have to load...
	

Installation:
	Just drop it in the extensions folder of the markdown package. (markdown/extensions)

Usage / Setup:
	Default Prefix is "icon-":
		In a Django Template: 
			{{ textmd|markdown:"safe,iconfonts" }}

		In Python:
			md = markdown.Markdown(extensions=['iconfonts'])
			converted_text = md.convert(text)


	Use a custom Prefix:
		In a Django Template:
			{{ textmd|markdown:"safe,iconfonts(prefix=mypref-)" }}

		In Python:
			md = markdown.Markdown(extensions=['iconfonts(prefix=mypref-)'])
			converted_text = md.convert(text)


	Use no prefix (just in case you couldn't figure it out :P):
		In a Django Template:
			{{ textmd|markdown:"safe,iconfonts(prefix=)" }}

		In Python:
			md = markdown.Markdown(extensions=['iconfonts(prefix=)'])
			converted_text = md.convert(text)



Copyright 2013 [Eric Eastwood](http://ericeastwood.com/)

Use it in any personal or commercial project you want.

"""

import markdown

# Global Vars
# Capture "&icon-namehere;" or "&icon-namehere:2x;" or "&icon-namehere:2x,muted;"
# https://www.debuggex.com/r/weK9ehGY0HG6uKrg
PREFIX = r'icon-'
ICON_RE_BEGIN = r'&'
ICON_RE_END = r'(?P<name>[a-zA-Z0-9-]+)(:(?P<mod>[a-zA-Z0-9-]+(,[a-zA-Z0-9-]+)*)){0,1};'
# This is the full regex we use. Only reason we have pieces above is to easily change the prefix to something custom
ICON_RE = ICON_RE_BEGIN + PREFIX + ICON_RE_END

class IconFontsPattern(markdown.inlinepatterns.Pattern):
	
	def __init__(self, pattern, m, configs):
		super(IconFontsPattern, self).__init__(pattern, m)

		self.config = configs

	""" Return a <i> element with the necessary classes"""
	def handleMatch(self, m):
		d = m.groupdict()
		
		el = markdown.util.etree.Element("i")

		modClassesString = ""
		if(d.get("mod")):
			modClassesString = " " + ' '.join((self.config['prefix'][0] + c) for c in d.get("mod").split(",") if c)

		el.set('class', self.config['prefix'][0] + d.get("name") + modClassesString)
		el.set('aria-hidden', 'true') # This is for Accessibility and text-to-speech browsers so they don't try to pronounce it
		return el

class IconFontsExtension(markdown.Extension):
	""" IconFonts Extension for Python-Markdown. """

	def __init__(self, configs):
		# define default configs
		self.config = {
			'prefix': ['icon-', "Custom class prefix."]
		}

		# Override defaults with user settings
		for key, value in configs:
			# convert strings to booleans
			if value == 'True': value = True
			if value == 'False': value = False
			if value == 'None': value = None

			self.setConfig(key, value)

		# Change prefix to what they had the in the config
		changePrefix(self.config['prefix'][0])


	def extendMarkdown(self, md, md_globals):
		md.inlinePatterns['iconfonts'] = IconFontsPattern(ICON_RE, md, self.config)

		md.registerExtension(self)


def makeExtension(configs=None):
	return IconFontsExtension(configs)


def changePrefix(prefix):
	global PREFIX, ICON_RE_BEGIN, ICON_RE_END, ICON_RE

	PREFIX = prefix
	ICON_RE = ICON_RE_BEGIN + PREFIX + ICON_RE_END