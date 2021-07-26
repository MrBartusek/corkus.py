![corkus banner](https://i.imgur.com/Cg7Apc2.jpg)

# Corkus.py ⚙️

> Asynchronous & Blazingly-Fast Python wrapper for [Public Wynncraft API](https://docs.wynncraft.com).
 
## Other libraries

There are a couple of other python wrappers for Wynncraft API and this is a comparison of their features to Corkus.py

| Feature | **Corkus.py** | [wynncraft-python](l3) | [Wynn.py](l1) | [Pynn](l2) |
| -------------------- | :-: | :-: | :-: | :-: |
| Full Coverage of API | ✔️ | ✔️ | ✔️ | ❌ |
| Rate-Limit           | ✔️ | ✔️ | ❌ | ❌ |
| Asynchronous         | ✔️ | ❌ | ❌ | ❌ |
| Return real objects  | ✔️ | ❌ | ❌ | ❌ |
| Typing               | ✔️ | ❌ | ❌ | ❌ |

### Why Corkus.py is better
**Asynchronous** - This is the only one libiary that uses asynchronous requests module [aiohttp](https://docs.aiohttp.org/en/stable/). That makes Corkus.py sutable when creating applications such as discord bots using [discord.py](https://discordpy.readthedocs.io/).

**Real Objects** - Corkus.py provides instances of real classes which mean your editor will autocomplete variables from all of the responses. In contrast other libraries return responses in dictionaries strings or, in the [Wynn.py](l1) case, [objects generated from dictionaries](https://github.com/Zakru/wynn.py/blob/eb7b7872d8720e56f01c0baba0c1b8a243c62ec4/wynn/requests.py#L154-L183). All of these solutions are viable but don't support *IntelliSense* of your IDE.

**Typing** - Same as *Real Objects* Corkus.py supports [typing](https://docs.python.org/3/library/typing.html) module which improves *IntelliSense* of your IDE.


[l1]: https://github.com/Zakru/wynn.py
[l2]: https://github.com/KashEight/Pynn
[l3]: https://github.com/martinkovacs/wynncraft-python
