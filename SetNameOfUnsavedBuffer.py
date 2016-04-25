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
    A Sublime Text plugin to set the displayed name of an unsaved buffer.
    """

    def run(self, edit):
        """
        Called when the plugin is run by the user.
        """

        # Abort the plugin if there is a file loading in the buffer.

        if self.view.is_loading():
            msg = "set_name_of_unsaved_buffer plugin: a file is loading in this buffer"
            sublime.status_message(msg)
            return

        # Abort the plugin if the buffer contains a saved file.

        if self.view.file_name() is not None:
            msg = "set_name_of_unsaved_buffer plugin: this buffer contains a saved file"
            sublime.status_message(msg)
            return

        # Open an input panel for the user to enter a name for the unsaved buffer.

        msg =  "Enter a name for the unsaved buffer:"
        self.view.window().show_input_panel(msg, "", self.on_done, None, None)


    def on_done(self, text):
        """
        Called when the user accepts the input panel.
        """

        # Abort the plugin if the user did not enter any text in the input panel.

        if len(text) < 1:
            msg = "set_name_of_unsaved_buffer plugin: nothing was entered in the panel"
            sublime.status_message(msg)
            return

        # Set the name of the unsaved buffer.

        self.view.set_name(text)
