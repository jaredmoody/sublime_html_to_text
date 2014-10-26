import sublime, sublime_plugin
import HTML2Text.html2text


class HtmlToTextFromFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    source = self.view.file_name()
    target = source + '.md'
    with open(source, 'r') as f:
      html = f.read()
    text = HTML2Text.html2text.html2text(html)
    if text != None:
      with open(target, 'w') as f:
        f.write(text)
      self.view.window().open_file(target)

  def is_enabled(self):
    return True

class HtmlToTextFromSelectionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        html = self.view.substr(region)
        text = HTML2Text.html2text.html2text(html)
        if text != None:
          self.view.replace(edit, region, text)

  def is_enabled(self):
    return True

class HtmlToTextFromClipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    html = sublime.get_clipboard()
    text = HTML2Text.html2text.html2text(html)
    if text != None:
      for region in self.view.sel():
        self.view.replace(edit, region, text)

  def is_enabled(self):
    return True

