# PyBot

invite [here](https://discord.com/oauth2/authorize?client_id=1091254412846051338&permissions=8&scope=bot)


# consigne 

[here](https://github.com/LordPouic/Python/blob/main/Projet%20Bot%20B2)



# requirements

```sh
pip install -r requirements.txt
```

and python 3.10 or newer

# configuration

get your token [here](https://discord.com/developers/applications)

create a file named `.env` and put your token in it like this:

```env
DISCORD_TOKEN=your_token
```

or you can use flags

```sh
python main.py --token your_token
```

---------------------------------------------

```sh
python main.py -t your_token
```

# commandes


## message prefix

prefix: `!`

| command     | description                             |
|-------------|-----------------------------------------|
| `!help`     | display help                            |
| `!ping`     | display `pong`                          |
| `!delete n` | delete `n` message (by default `n` = 1) |


## slash commands


| command            | description                                                |
|--------------------|------------------------------------------------------------|
| `/ping`            | display `pong` (ephemeral)                                 |
| `/github username` | display GitHub user info (or by default username = `tot0p` |
|`/about`            | display bot info                                           |

### commands groups

#### history

| command            | description                                                |
|--------------------|------------------------------------------------------------|
| `/show`            | display history in embed pagination                        |
| `/show_all`        | display all history in one message                         |
| `/last`            | display last command                                       |
| `/clear`           | clear history                                              |

#### role

| command            | description                                                |
|--------------------|------------------------------------------------------------|
| `/add nameOfRole username`            | add role to user                        |
| `/remove nameOfRole username`        | remove role from user                    |
| `/create nameOfRole`            | create role                                   |

#### send


| command                                | description                                                |
|----------------------------------------|------------------------------------------------------------|
| `/send mp username message`            | send message to user                                       |
