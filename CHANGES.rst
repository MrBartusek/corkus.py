Change Log
==========

Corkus.py follows `semantic versioning <http://semver.org/>`_. Due to ever changing nature of Wynncraft API only the
newest version is supported. Please ensure that you are always using the newest version.

.. py:currentmodule:: corkus

3.1.0 (2024/04/29) 
----------------------

Corkus.py is no longer maintained. For more information please see: `README <https://github.com/MrBartusek/corkus.py#readme>`_.

- Add ``DeprecationWarning`` to module ``__init__``
- Add deprecation notices to ``README.MD`` and ``docs/index.rst``

3.0.1 (2022/12/02) 
----------------------

- Update documentation front page.
- Update documentation guides - :ref:`discord`, :ref:`quickstart`
- Other minor documentation fixes.

3.0.0 (2022/12/01) 
----------------------

We are making changes due to the `2.0.1 API update <https://forums.wynncraft.com/threads/2-0-1-full-changelog.304461/>`_
which brings some changes around player classes. We have also changed initialization procedure so client constructor doesn't need to
be called in async context anymore. We are introducing a concept like other async libraries. You now need to call ``start()``
function to initialize the client.

- :bdg-danger-line:`BREAKING` :py:class:`Corkus` initialization procedure have been changed. You now need to call
  :py:func:`Corkus.start() <Corkus.start>` to initialize the client.

  .. code-block:: python
    :emphasize-lines: 4

    corkus = Corkus(timeout=60)

    async def main():
        await corkus.start()

        player = await corkus.player.get("MrBartusekXD")
        print(player.best_character.combat.level) # 102

        await corkus.close()

- :bdg-danger-line:`BREAKING` Due to recent API changes ``Character.name`` (formerly: ``PlayerClass.name``) was removed.

- :bdg-danger-line:`BREAKING` Ability to pass custom ``ClientSession`` to :py:class:`Corkus` was removed.

- :bdg-danger-line:`BREAKING` :py:class:`Corkus` configuration option ``ratelimit_enable`` and ``cache_enable``
  were renamed to ``disable_ratelimit`` and ``disable_cache`` respectively. Their function were reversed and
  are both now respectively disabled by default.

- :bdg-warning-line:`Deprecated` ``Player.classes`` and ``Player.best_class`` were deprecated,
  use :py:attr:`Player.characters <corkus.objects.Player.characters>` and
  :py:attr:`Player.best_character <corkus.objects.Player.best_character>` instead. These will now return instancies
  of :py:class:`Character <corkus.objects.Character>` which are identical to ``PlayerClass`` excluding the ``name`` property.

- ``PlayerClass`` was renamed to :py:class:`Character <corkus.objects.Character>` to match new API schema.

- ``ClassType`` was renamed to :py:class:`CharacterType <corkus.objects.CharacterType>` to match new API schema.

- Add :py:attr:`uuid <corkus.objects.Character.uuid>` property to :py:class:`Character <corkus.objects.Character>` (formerly: ``PlayerClass``).

- Project now uses ``characters`` instead of ``classes`` in documentation.

- Default request timeout was changed to ``60`` seconds.

- Add support for `Python 3.11 <https://docs.python.org/3/whatsnew/3.11.html>`_.

- Update dependencies. You can now use ``aiohttp 3.8.x`` and ``iso8601 1.x``.

- Fix :py:exc:`CorkusTimeoutError <corkus.errors.CorkusTimeoutError>` returning invalid url.

.. py:currentmodule:: corkus.objects

2.0.0 (2022/06/07)
------------------

- :bdg-danger-line:`BREAKING` Due to recent API changes ``PlayerStatistics.chests_found`` and
  ``ClassStatistics.chests_found`` were removed.
- :bdg-danger-line:`BREAKING` Value of :py:attr:`ServerType.REGULAR` has been changed from ``WC`` to ``REGULAR``.
- :bdg-danger-line:`BREAKING` ``ServerType.YOUTUBE`` enum key is now named :py:attr:`ServerType.MEDIA` and it's 
  value has been changed from ``YT`` to ``MEDIA``.
- Add warnings for broken properties in :py:class:`PlayerSoloRanking` and :py:class:`PlayerOverallRanking`.

1.2.1 (2022/01/20)
------------------

- Fix a bug where :py:exc:`CorkusTimeoutError <corkus.errors.CorkusTimeoutError>` will be thrown without timeout property
  when no custom timeout is set (`#13 <https://github.com/MrBartusek/corkus.py/pull/13>`_)

1.2.0 (2021/12/26)
------------------

- Add :py:func:`get_member() <Guild.get_member>` function to :py:class:`Guild`.
- Add :py:attr:`rank <Member.rank>` property to :py:class:`Member`.
- Add ``best_class <Player.best_class>`` property to :py:class:`Player`.
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
