
## Set Name Of Unsaved Buffer - Plugin for Sublime Text

This is a simple Sublime Text plugin which allows the user to quickly and easily set the name of an unsaved buffer so that the name is shown in the buffer's name tab, in the side bar, in the drop-down list of buffers, and in the show files overlay. The purpose of the plugin is so that temporary buffers can be conveniently given a name and thereby switched to easily, this is especially useful if there are more than one temporary buffers in use.

When the plugin is run it will display an input panel for the user to enter a name for the unsaved buffer. The plugin can only be run from unsaved buffers.

It is such a simple plugin that there are no plans to submit it to [Package Control](http://packagecontrol.io).

#### Requirements

- Sublime Text v2 or v3

#### Installation

###### Manual Installation

- Download this repository's [ZIP file](https://github.com/mattst/sublime-set-name-of-unsaved-buffer/archive/master.zip) and extract it or use `git clone` to get the files.

- Rename the extracted folder to `SetNameOfUnsavedBuffer` and move the folder to your Sublime Text config `Packages` folder so that you end up with (the exact path depends on your OS and Sublime Text version):

    - Linux: `~/.config/sublime-text-3/Packages/SetNameOfUnsavedBuffer/`
    - OS X: `~/Library/Application Support/Sublime Text 3/Packages/SetNameOfUnsavedBuffer/`
    - Windows: `%APPDATA%\Sublime Text 3\Packages\SetNameOfUnsavedBuffer\`

###### Package Control

This package has not been submitted to the official [Package Control](http://packagecontrol.io) channel but Package Control can install single repositories, see *Add Repository* in the [Package Control usage section](https://packagecontrol.io/docs/usage).

To install:

- Open the Command Palette and select: `Package Control: Add Repository`
- Paste this url into the input panel: `https://github.com/mattst/sublime-set-name-of-unsaved-buffer`
- Open the Command Palette and select: `Package Control: Install Package`
- Select: `Set Name Of Unsaved Buffer`

If updates are made to this package then Package Control will install them automatically as usual.

To uninstall:

- Open the Command Palette and select: `Package Control: Remove Package`
- Select: `Set Name Of Unsaved Buffer`
- Open the Command Palette and select: `Package Control: Remove Repository`
- Select: `https://github.com/mattst/sublime-set-name-of-unsaved-buffer`


#### Usage

The plugin automatically adds a `Set Name of Unsaved Buffer` entry to the command palette, although it will only be displayed if the currently active buffer is unsaved.

If you want you can add a key binding for the plugin in your `sublime-keymap` file (`Menu --> Preferences --> Key Bindings - User`):

    { "keys": ["ctrl+whatever"], "command": "set_name_of_unsaved_buffer" }

I use `"ctrl+k", "ctrl+n"` which was not in use by default on my system:

    { "keys": ["ctrl+k", "ctrl+n"], "command": "set_name_of_unsaved_buffer" }

#### License

This plugin is licensed under The MIT License (MIT), see the LICENSE file.
