# Modsync Server

This is the API for the [Modsync](https://github.com/Sit-Back/modsync) app.
## API
### Metadata
Metadata is at `/meta` and is constructed as follows:
1. Loader ID as found in the Minecraft Launcher versions directory. This is to add to the launcher profile to launch  the correct version.
2. Loader silent install command to run on the loader to install. The java at the front is not included and all %1s in the string will be replaced with the .minecraft directory of the user. %2s will be replaced with the loader location.
3. A list of mods on the server each taking up one line. This is for the client to compare differences to sync.

### Misc Routes

| Route             | Description                                                                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/app`            | Windows download of the Modsync App.                                                                                                               |
| `/loader`         | A download for the loader installer, this is provided separately to increase download speeds and provide offline installers for supported loaders. |
| `/mods/<modname>` | Download the mod with that name.                                                                                                                   |
