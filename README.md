
## Set Name Of Unsaved Buffer - Plugin for Sublime Text

This is a simple Sublime Text plugin which allows the user to quickly and easily set the name of an unsaved buffer so that the name is shown in the buffer's file tab, in the drop-down list of files, and in the show files overlay.

When the plugin is run it will display an input panel for the user to enter a name for the unsaved file. The plugin will not allow users to change the name of a saved file for obvious reasons. [Note that entering a path as the name is inadvisable because the file's name would be a path but no path would be set.]

It is such a simple plugin that there are no plans to submit it to [Package Control](http://packagecontrol.io), so anyone who wants to use it will have to install it manually.

#### Requirements / Tested

- Sublime Text v2 or v3
- Tested with: v2 build 2221 and v3 build 3103

#### Installation

Manual installation only.

- Download this repository's [ZIP file](https://github.com/mattst/sublime-set-name-of-unsaved-buffer/archive/master.zip) and extract it or use `git clone` to get the files.

- Move the `SetNameOfUnsavedBuffer.py` file to the subdirectory of your choice in the Sublime Text config `Packages` directory. e.g. (the exact path depends on your OS and Sublime Text version):
  - `~/.config/sublime-text-3/Packages/User/SetNameOfUnsavedBuffer.py`
  - `~/.config/sublime-text-3/Packages/MiscPlugins/SetNameOfUnsavedBuffer.py`
  - `~/.config/sublime-text-3/Packages/SetNameOfUnsavedBuffer/SetNameOfUnsavedBuffer.py`

That's it.

#### Setup

The plugin's command is: `set_name_of_unsaved_buffer`

Add a key binding in your `Default (OS).sublime-keymap` file (`Menu --> Preferences --> Key Bindings - User`):

    { "keys": ["ctrl+whatever"], "command": "set_name_of_unsaved_buffer" }

If you prefer to start the plugin from the command palette add the line below to `~/.config/sublime-text-3/Packages/User/Default.sublime-commands` (or equivalent directory location):

    { "caption": "Set Name of Unsaved Buffer", "command": "set_name_of_unsaved_buffer" }

If you don't already have a `.../User/Default.sublime-commands` file, for your own custom commands, just create it and add the following.

    [
        { "caption": "Set Name of Unsaved Buffer", "command": "set_name_of_unsaved_buffer" }
    ]

Advanced users will be aware that there are many alternatives to setting up this plugin.

#### Bugs

This plugin has no known bugs however, while writing it, a bug in Sublime Text v3 (build 3103) was found which can affect the plugin. The [bug report](https://github.com/SublimeTextIssues/Core/issues/1180) is here. The bug is not present in Sublime Text v2 (build 2221).

If an unsaved file in a buffer has already been given a name and then that name is changed, the new name will not be shown until after some kind of modification has been made to the unsaved file. So just enter a new line or a single character and the new name will be shown correctly.

#### License

This plugin is licensed under The MIT License (MIT), see the LICENSE file.
