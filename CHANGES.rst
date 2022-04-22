Change Log
==========

Corkus.py follows `semantic versioning <http://semver.org/>`_.

.. py:currentmodule:: corkus.objects


1.2.1 (2022/01/20)
------------------

- Fix a bug where :py:exc:`CorkusTimeoutError <corkus.errors.CorkusTimeoutError>` will be thrown without timeout property
  when no custom timeout is set (`#13 <https://github.com/MrBartusek/corkus.py/pull/13>`_)

1.2.0 (2021/12/26)
------------------

- Add :py:func:`get_member() <Guild.get_member>` function to :py:class:`Guild`.
- Add :py:attr:`rank <Member.rank>` property to :py:class:`Member`.
- Add :py:attr:`best_class <Player.best_class>` property to :py:class:`Player`.
- :py:func:`OnlinePlayers.get_player_server` and :py:func:`OnlinePlayers.is_player_online` now accept :py:class:`Member` as argument.
- Support `Python 3.10 <https://docs.python.org/3/whatsnew/3.10.html>`_

1.1.0 (2021/10/02)
------------------

- Add new server type :py:attr:`ServerType.OTHER` to :py:class:`ServerType`.
- Fix :py:attr:`Guild.level` and :py:attr:`LeaderboardGuild.level` documentation.
- Standardize documentation of :py:class:`Player` and :py:class:`PartialPlayer` properties.
- Fix :py:class:`PartialOnlinePlayer` ``__repr__``

1.0.0 (2021/09/09)
------------------

- 🎉 first release!
