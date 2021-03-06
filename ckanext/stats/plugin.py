from logging import getLogger

import ckan.plugins as p

log = getLogger(__name__)

class StatsPlugin(p.SingletonPlugin):
    '''Stats plugin.'''

    p.implements(p.IRoutes, inherit=True)
    p.implements(p.IConfigurer, inherit=True)

    def after_map(self, map):
        map.connect('stats', '/stats',
            controller='ckanext.stats.controller:StatsController',
            action='index')
        map.connect('stats_action', '/stats/{action}',
            controller='ckanext.stats.controller:StatsController')
        return map

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
