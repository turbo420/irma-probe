import logging

from probes.database.database import DatabaseProbe


log = logging.getLogger(__name__)

class NSRLProbe(DatabaseProbe):
    
    ##########################################################################
    # plugin metadata
    ##########################################################################

    _plugin_name = "NSRL"
    _plugin_version = "0.0.0"
    _plugin_description = "Information plugin to query hashes on NRSL database"

    ##########################################################################
    # constructor and destructor stuff
    ##########################################################################

    def __init__(self, conf=None, *args, **kwargs):
        # TODO: move api key in a configuration file
        nsrl_os_db = conf.get('nsrl_os_db', None) if conf else None
        nsrl_mfg_db = conf.get('nsrl_mfg_db', None) if conf else None
        nsrl_file_db = conf.get('nsrl_file_db', None) if conf else None
        nsrl_prod_db = conf.get('nsrl_prod_db', None) if conf else None
        # call super classes constructors
        super(NSRLProbe, self).__init__(conf, **kwargs)
        # NSRL modules does late import, may fail here
        self._module = None
        try:
            # late imports
            global NSRL
            from modules.database.nsrl import NSRL
            self._module = NSRL(nsrl_file_db, nsrl_prod_db, nsrl_os_db, nsrl_mfg_db)
        except Exception as e:
            print e
            log.exception(e)