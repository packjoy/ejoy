class TemplateLoader(object):
	def __init__(self, template_name, *args, **kwargs)
		self.template = self.load_template(template_name=template_name)

	def load_template(self, template_name, *args, **kwargs):
		return render_template('mail/{}.html'.format(template_name), *args, **kwargs)