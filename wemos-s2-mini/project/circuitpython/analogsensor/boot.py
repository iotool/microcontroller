# disable write protection
import storage
storage.remount("/", False)

# disable auto reload
import supervisor
supervisor.disable_autoreload()