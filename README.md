
## Set Name Of Unsaved Buffer - Plugin for Sublime Text

This is a simple Sublime Text plugin which allows the user to quickly and easily set the name of an unsaved buffer so that the name is shown in the buffer's name tab, in the side bar, in the drop-down list of buffers, and in the show files overlay. The purpose of the plugin is so that temporary buffers can be conveniently given a name and thereby switched to easily, this is especially useful if there are more than one temporary buffers in use.

When the plugin is run it will display an input panel for the user to enter a name for the unsaved buffer. The plugin will not change the name of a saved buffer for obvious reasons. Clearly entering a path as the name is inadvisable because the buffer's name would be a path but no path would be set.

It is such a simple plugin that there are no plans to submit it to [Package Control](http://packagecontrol.io), so anyone who wants to use it will have to install it manually.

#### Requirements

- Sublime Text v2 or v3

#### Installation

Manual installation only.

- Download this repository's [ZIP file](https://github.com/mattst/sublime-set-name-of-unsaved-buffer/archive/master.zip) and extract it or use `git clone` to get the files.

- Rename the extracted folder to `SetNameOfUnsavedBuffer` and move the folder to your Sublime Text config `Packages` folder so that you end up with (the exact path depends on your OS and Sublime Text version):

    - `Linux:    ~/.config/sublime-text-3/Packages/SetNameOfUnsavedBuffer/`
    - `OS X:     ~/Library/Application Support/Sublime Text 3/Packages/SetNameOfUnsavedBuffer/`
    - `Windows:  %APPDATA%\Sublime Text 3\Packages\SetNameOfUnsavedBuffer\`

#### Usage

The plugin automatically adds a `Set Name of Unsaved Buffer` entry to the command palette, although it will only be displayed if the currently active buffer is unsaved.

If you want you can add a key binding for the plugin in your `Default (OS).sublime-keymap` file (`Menu --> Preferences --> Key Bindings - User`):

    { "keys": ["ctrl+whatever"], "command": "set_name_of_unsaved_buffer" }

I use `"ctrl+k", "ctrl+n"` which was not in use by default on my system:

    { "keys": ["ctrl+k", "ctrl+n"], "command": "set_name_of_unsaved_buffer" }

#### License

This plugin is licensed under The MIT License (MIT), see the LICENSE file.
