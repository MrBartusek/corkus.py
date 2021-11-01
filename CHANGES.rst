Change Log
==========

Corkus.py follows `semantic versioning <http://semver.org/>`_.

.. py:currentmodule:: corkus.objects

Upcoming Changes
----------------

- Add :py:func:`get_member() <Guild.get_member>` function to :py:class:`Guild`.
- Add :py:attr:`rank <Member.rank>` property to :py:class:`Member`.
- :py:func:`OnlinePlayers.get_player_server` and :py:func:`OnlinePlayers.get_player_server` now accept :py:class:`Member` as argument.

1.1.0 (2021/10/02)
------------------

- Add new server type :py:attr:`ServerType.OTHER` to :py:class:`ServerType`.
- Fix :py:attr:`Guild.level` and :py:attr:`LeaderboardGuild.level` documentation.
- Standardize documentation of :py:class:`Player` and :py:class:`PartialPlayer` properties.
- Fix :py:class:`PartialOnlinePlayer` ``__repr__``

1.0.0 (2021/09/09)
------------------

- 🎉 first release!
