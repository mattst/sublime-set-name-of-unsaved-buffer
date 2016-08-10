
#
# Name:          Set Name Of Unsaved Buffer
#
# Requirements:  Plugin for Sublime Text v2 and v3
#
# Written by:    mattst - https://github.com/mattst
#
# ST Command:    set_name_of_unsaved_buffer
#
# License:       MIT License
#

import sublime, sublime_plugin


def is_sublime_text_3():
    return 3000 <= int(sublime.version()) <= 3999


class SetNameOfUnsavedBufferCommand(sublime_plugin.TextCommand):
    """
    A Sublime Text plugin to set the name of an unsaved buffer. The name will
    be shown in the files tab bar, in the side bar, in the drop-down files
    list, and in the show files overlay. The purpose of the plugin is so that
    temporary buffers can be quickly given a name and then switched to easily,
    this is especially useful if more than one temporary buffer is in use. The
    plugin can take an optional boolean "set_scratch" arg which will set the
    buffer's 'scratch' status, this controls whether or not a save prompt will
    be shown when the buffer is closed, i.e. no save prompt if set to true.
    """

    def is_enabled(self):

        # Only enables the plugin for unsaved buffers.

        if (self.view.file_name()
         or self.view.is_loading()
         or self.view.settings().get("is_widget")):
            msg = "the plugin can only be run from an unsaved buffer"
            sublime.status_message(msg)
            return False

        return True


    def run(self, edit, **kwargs):

        self.handle_set_scratch_setting(**kwargs)

        msg =  "Enter a name for the unsaved buffer:"

        self.view.window().show_input_panel(msg, "",
                           self.on_panel_done, None, None)


    def handle_set_scratch_setting(self, **kwargs):

        setting_name = "set_scratch"

        if setting_name in kwargs:
            setting_value = kwargs.get(setting_name)
            if isinstance(setting_value, bool):
                self.view.set_scratch(setting_value)


    def on_panel_done(self, name_for_buffer):

        name_for_buffer = name_for_buffer.strip()

        if not name_for_buffer:
            msg = "no name was entered for the unsaved buffer"
            sublime.status_message(msg)
            return

        self.view.set_name(name_for_buffer)

        # The bug workaround must be performed by a new TextCommand
        # because an 'edit' object is required for text insertions,
        # and this class's 'edit' object expires when run() returns.

        if is_sublime_text_3():
            command_name = "set_name_of_unsaved_buffer_bug_workaround"
            self.view.window().run_command(command_name)


class SetNameOfUnsavedBufferBugWorkaroundCommand(sublime_plugin.TextCommand):
    """
    There is a bug in Sublime Text 3 when using set_name() to set the name of
    an unsaved buffer. After assigning the new name it will not be displayed
    until after the buffer has been modified in some way, i.e. a character is
    inserted or deleted. This command is a workaround for that bug and it just
    inserts a space at the end of the buffer and then immediately deletes it.
    Bug report @: https://github.com/SublimeTextIssues/Core/issues/1180
    """

    def run(self, edit):

        end_pos = self.view.size()

        num_chars_inserted = self.view.insert(edit, end_pos, " ")

        if num_chars_inserted == 1:
            erase_region = sublime.Region(end_pos, end_pos + 1)
            self.view.erase(edit, erase_region)
