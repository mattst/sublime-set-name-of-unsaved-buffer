
#
# Name:      Set Name Of Unsaved Buffer
#
# Requires:  Sublime Text v2 or v3 (plugin)
#
# Command:   set_name_of_unsaved_buffer
#
# Author:    mattst - https://github.com/mattst
#
# Web Page:  https://github.com/mattst/sublime-set-name-of-unsaved-buffer
#
# License:   MIT License
#


import sublime, sublime_plugin


def is_sublime_text_3():
    return 3000 <= int(sublime.version()) <= 3999


class SetNameOfUnsavedBufferCommand(sublime_plugin.TextCommand):
    """
    A Sublime Text plugin to set the name of an unsaved buffer. The name will
    be shown in the buffer's tab, in the side bar, in the drop-down files list
    and in the show files overlay. Its purpose is so that temporary buffers can
    be conveniently and quickly given a name and then switched to easily, this
    is especially useful if there are several temporary buffers in use.
    """

    def is_enabled(self):

        # The plugin is only enabled for unsaved buffers.

        return self.view.file_name() is None


    def run(self, edit):

        # Prevent the user from attempting to
        # change the name of a panel or overlay.

        if self.view.settings().get("is_widget"):
            msg = "run from an unsaved buffer not a panel or overlay"
            sublime.status_message(msg)
            return

        msg =  "Enter a name for the unsaved buffer:"

        self.view.window().show_input_panel(msg, "",
                           self.on_panel_done, None, None)


    def on_panel_done(self, buffer_name):

        buffer_name = buffer_name.strip()

        if not buffer_name:
            return

        self.view.set_name(buffer_name)

        # The bug workaround must be done by another TextCommand;
        # an edit object is needed for it and the edit object that
        # was passed to run() expired as soon as run() returned.

        if is_sublime_text_3():
            command_name = "set_name_of_unsaved_buffer_bug_workaround"
            self.view.run_command(command_name)


class SetNameOfUnsavedBufferBugWorkaroundCommand(sublime_plugin.TextCommand):
    """
    There is a bug in Sublime Text 3 when using set_name(); in some cases when
    it is called the new name will not get properly set until after the buffer
    has been altered, i.e. a character is inserted or deleted. This class is a
    workaround for that bug and it simply inserts and deletes a space at the
    end of the buffer. The bug is not present in Sublime Text 2. More info is
    in my bug report @: https://github.com/SublimeTextIssues/Core/issues/1180
    """

    def run(self, edit):

        single_space = " "
        pos = self.view.size()
        if self.view.insert(edit, pos, single_space) == 1:
            self.view.erase(edit, sublime.Region(pos, pos + 1))
