#
# Name:           Set Name Of Unsaved Buffer
#
# File:           SetNameOfUnsavedBuffer.py
#
# Written by:     mattst - https://github.com/mattst
#
# Requirements:   Plugin for Sublime Text v2 and v3
#
# ST Command:     set_name_of_unsaved_buffer
#

import sublime, sublime_plugin

class SetNameOfUnsavedBuffer(sublime_plugin.TextCommand):
    """
    A Sublime Text plugin to set the name of an unsaved buffer. The name will be shown
    in the files tab bar, in the side bar, in the drop-down files list, and in the show
    files overlay. The purpose of the plugin is so that temporary buffers can be given
    a name and thereby switched to easily, this is especially useful if more than one
    temporary buffer is in use. Note that entering a path as the name is inadvisable
    because the file's name would be a path but no path would be set.
    """

    def run(self, edit):
        """
        Called when the plugin is run by the user.
        """

        # Abort the plugin if a file is loading in the buffer, if the buffer contains
        # a saved file, or if the plugin has been run from a widget (panel or overlay).

        if self.view.is_loading():
            self.show_error_message("a file is loading in this buffer")
            return

        if self.view.file_name():
            self.show_error_message("this buffer contains a saved file")
            return

        if self.view.settings().get('is_widget'):
            self.show_error_message("run from a buffer not from a panel or overlay")
            return

        # Open an input panel for the user to enter a name for the unsaved buffer.

        msg =  "Enter a name for the unsaved buffer:"
        self.view.window().show_input_panel(msg, "", self.set_name, None, None)


    def set_name(self, name_for_buffer):
        """
        Called when the user accepts the input panel.
        """

        # Abort if the user did not enter any text in the input panel.

        if not name_for_buffer:
            self.show_error_message("no name was entered for the buffer")
            return

        # Set the name of the unsaved buffer.

        self.view.set_name(name_for_buffer)


    def show_error_message(self, err_msg):
        """
        Displays the error message "err_msg".
        """

        err_msg_prefix = "set_name_of_unsaved_buffer plugin: "
        sublime.status_message(err_msg_prefix + err_msg)
