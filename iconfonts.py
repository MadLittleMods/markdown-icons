"""
IconFonts Extension for Python-Markdown
========================================

Version: 2.1

Description:
	Use this extension to display icon font icons in python markdown. Just add the css necessary for your font and add this extension.

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
	Just drop it in the extensions folder of the markdown package. (markdown/extensions).
	Also check out: https://pythonhosted.org/Markdown/extensions/index.html

Usage/Setup:
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

	We also now support a base option which allows for Bootstrap 3 and FontAwesome 4
		In Python:
			md = markdown.Markdown(extensions=['iconfonts(base=icon)'])
			converted_text = md.convert(text)

		Input: `&icon-html5;`
		Output: `<i aria-hidden="true" class="icon icon-html5"></i>`

	Combine options with a comma:
		md = markdown.Markdown(extensions=['iconfonts(prefix=fa-, base=fa)'])
		

Copyright 2014 [Eric Eastwood](http://ericeastwood.com/)

Use it in any personal or commercial project you want.

"""

import markdown

class IconFontsExtension(markdown.Extension):
	""" IconFonts Extension for Python-Markdown. """

	def __init__(self, *args, **kwargs):

		# define default configs
		self.config = {
			'prefix': ['icon-', "Custom class prefix."],
			'base': ['', "Base class added to each icon"]
		}

		# Override defaults with user settings
		# This is legacy code for versions older than 2.5.1.
		if len(args):
			for key, value in args[0]:
				# convert strings to booleans
				if value == 'True': value = True
				if value == 'False': value = False
				if value == 'None': value = None

				self.setConfig(key, value)

		# Override defaults with user settings
		# This is not legacy code but is used instead of the super call below because we have to support the legacy version
		if hasattr(self, 'setConfigs'):
			self.setConfigs(kwargs)

		
		# We can use this instead of the legacy for loop to set the config above
		#super(IconFontsExtension, self).__init__(*args, **kwargs)


	def extendMarkdown(self, md, md_globals):
		config = self.getConfigs();
		#print("config" + str(config))

		md.registerExtension(self)

		# Change prefix to what they had the in the config
		# Capture "&icon-namehere;" or "&icon-namehere:2x;" or "&icon-namehere:2x,muted;"
		# https://www.debuggex.com/r/weK9ehGY0HG6uKrg
		prefix = config['prefix']
		icon_regex_start = r'&'
		icon_regex_end = r'(?P<name>[a-zA-Z0-9-]+)(:(?P<mod>[a-zA-Z0-9-]+(,[a-zA-Z0-9-]+)*)){0,1};'
		# This is the full regex we use. Only reason we have pieces above is to easily change the prefix to something custom
		icon_regex = icon_regex_start + prefix + icon_regex_end

		md.inlinePatterns['iconfonts'] = IconFontsPattern(icon_regex, md, config)


# http://pythonhosted.org/Markdown/extensions/api.html#makeextension
def makeExtension(*args, **kwargs):
	return IconFontsExtension(*args, **kwargs)



class IconFontsPattern(markdown.inlinepatterns.Pattern):
	
	def __init__(self, pattern, md, config):
		# Pass the patterna and markdown instance
		super(IconFontsPattern, self).__init__(pattern, md)

		self.config = config

	""" Return a <i> element with the necessary classes"""
	def handleMatch(self, match):

		# The dictionary keys come from named capture groups in the regex
		match_dict = match.groupdict()
		
		# Create the <i> element
		el = markdown.util.etree.Element("i")

		# Mods are modifier classes. The syntax in the markdown is "&icon-namehere:2x;" and with multiple "&icon-spinner:2x,spin;"
		mod_classes_string = ""
		if(match_dict.get("mod")):
			# Make a string with each modifier like: " icon-2x iconspin"
			mod_classes_string = " " + ' '.join((self.config['prefix'] + c) for c in match_dict.get("mod").split(",") if c)

		base_class = ""
		if(self.config['base']):
			base_class = self.config['base'] + " "

		icon_class = self.config['prefix'] + match_dict.get("name")

		# Add the icon classes to the <i> element
		el.set('class', base_class + icon_class + mod_classes_string)
		# This is for accessibility and text-to-speech browsers so they don't try to read it
		el.set('aria-hidden', 'true')
		return el