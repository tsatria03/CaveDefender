CaveDefender.

CaveDefender is an online, audio only game. You sign in to an account on a server and share a world with other players: you chat, move around together, make rooms, and play the cave defender game, where you gather wood and defend four walls against waves of enemies, or, in the reverse mode, attack the walls from outside while bots defend them. This readme explains how everything works. For the list of typed chat commands, type /help in the game, which opens the player help.

Moving around.

You move with the arrow keys, and holding alt while you move makes you run. Press alt plus R at any time to toggle auto-running: when it is on you run by default and hold alt to walk instead, and when it is off it works the other way around. The game tells you auto running enabled or disabled as you switch it, and your choice is saved for next time.

Chat channels.

Slash opens global chat, which everyone on the server hears.
Backslash opens local chat, which only the people sharing your current space hear, whether that is the lobby or your room.
Apostrophe opens staff chat, which only staff can send to or hear; as a regular player you can't use it.
Semicolon opens team chat while you are in a game, which everyone on your team hears. For now every player in a game is on one team, so it reaches the whole game, but in the player versus player mode it will reach only your own side.

Global chat is also divided into language channels. You only hear global messages from people on the same language channel as you, so each language has its own conversation. Local chat, private messages, and staff chat all reach across channels, so local chat reaches everyone sharing your space whatever channel they are on. Choose your language with /channel, everyone starts on English, and your choice is saved for next time.

One of the channels is named Unfiltered. It works like any other channel, in that you only hear global chat from people who have also chosen it, but it is the one channel where the word filter is switched off for global chat. Local chat is always filtered no matter which channel you are on, since it reaches everyone sharing your space. Unfiltered is meant for talking freely, including adult or NSFW topics, so pick it only if you are happy to both read and write that kind of language. No one is ever put there automatically, and you can leave it any time by choosing another channel with /channel.

You can run any command from any chat you have access to.

Chat filtering.

Chat is filtered for forbidden words, a list set by the server's host. If a message you send contains one it is not delivered to anyone, and you are told that it contains forbidden words. Global chat skips this word filter only on the Unfiltered language channel; local chat is always filtered no matter your channel, and staff chat is not word filtered.

Separately, there is always-on protection against screen reader crash strings: character sequences that can crash text to speech engines such as Eloquence or IBMTTS when spoken aloud. This protection covers every chat channel, including Unfiltered, local, and staff, and cannot be turned off, so no one can crash other players' speech by sending one in chat.

Pronouns.

Messages that talk about you in the third person can use your pronouns, for example when you raise your staff flag, change your nickname, or join a room. Choose them with /pronoun, which opens a menu of the options the server offers, such as masculine, feminine, singular they, or one of several neopronoun sets. Everyone starts on singular they, and your choice is saved for next time. There is also a none option, which simply uses your name in place of a pronoun, so the message reads with your name rather than he, she, or they.

The players menu.

Press F6 anywhere to open the players menu, a list of everyone on the server shown by their away status, rank, name, and current language channel, the same people the /who command reads out.

Choose a player to open a read-only information card about them, showing their username, nickname, pronouns, language channel, rank, whether they are away, where they are, the lobby, a room, or a game, and the version of the game they are running. Staff see a few extra lines on the card about the player's mute, ban, and warning record. Press escape or close to leave the card.

The card also has a Mute this player checkbox, with the Alt plus M shortcut, and a Private message this player button, with Alt plus P.

Muting a player is personal and affects only you: while it is on you no longer see their global chat, local chat, or private messages, and you no longer hear their voice, while everyone else still does and the player is never told. It stays in effect across sessions until you open their card again and uncheck it.

The private message button asks you for a message and sends it straight to that player, the same as the /pm command. Your own card does not show either control, since you cannot mute or message yourself.

If you are staff, the card also shows action buttons for the things your rank lets you do to that player: kick, ban, promote, demote, notify, and warn. Only the buttons you are actually allowed to use on that particular player appear, and choosing one asks for anything it needs, such as a ban length, a new rank, a notification, or a warning level and reason, before carrying out the same action as the matching staff command. They never let you do anything the commands would not, so all the usual rank rules still apply; the staff help explains each of these in full.

Rooms.

From the lobby, press enter to open the lobby menu, where you can create or join a public or private room. You can host up to one public and one private room of your own.

Inside a room, press enter for the room menu. If you host the room you can use Kick from room to send a player back to the lobby, and, for a private room, set or retrieve its password. The Kick from room list also includes your own name, which you can pick to simply leave your own room, just like Leave room does. You can delete your own room, but only when you are the only one in it and no games are running.

Anyone in a room can invite someone to it. Choose Invite to room from the room menu to see everyone currently in the lobby, and pick the person you want. They are told privately that you invited them, and they join by typing /accept, or refuse with /reject; an invitation lasts two minutes before it expires. Accepting brings them straight in, even past a private room's password, and you are told whether they accepted or declined.

Games.

Inside a room you can start a game, choosing a game mode, then who can play, then a map size, and others can join your open games while a game still has room. There are two modes. This section describes the original, player versus environment, or PVE, where you defend four walls that each start at a random strength; the reverse mode, environment versus player, has its own section below. If you host the game, press enter for the round menu, where you begin the round.

If your game is open, that menu also has Invite to game and Kick from game, which are the same idea as the room's Invite to room and Kick from room but one step further in.

Invite to game first asks where to invite from, your room or the lobby, then lists the players there for you to pick; the player you pick answers the same way, with /accept or /reject. Choosing the lobby pulls someone straight into the cavern, past a private room's password, without their having to join the room first.

A player you invited from the lobby returns to the lobby when they leave the game or it ends, while a player who joined through your room returns to the room; Kick from game follows the same rule, sending each player back to wherever they came from. The Kick from game list also includes your own name, which you can pick to simply leave your own game, the same as leaving through the pause menu.

Anyone can press tab to hear the current round status, such as the build countdown or, once the wave is on, which round it is and whether the enemies are attacking or resting. Each fresh wave is also announced with its round number, for example round one, the enemies are coming, and that number climbs as the round wears on. About ten seconds before each wave, whether the first one at the end of the build phase or a later one after a rest, you get a heads-up sound and an alert telling you how long until the enemies attack.

The round opens with a build phase to prepare, and you begin each round already carrying ten to twenty starter wood so you can shore up a weak wall right away. More wood drops around the cavern, and simply walking near a piece picks up everything within five tiles of you.

Stand within five tiles of any wall and press shift plus enter to spend one piece reinforcing the nearest wall, no matter which way you face; the strength gained is random, and you can over-build a wall up to four times its full strength as a buffer, but no higher. You can reinforce during the build phase and during the rest periods between attacks, but not while the enemies are actively striking. Hold shift plus enter to keep placing wood without pressing it for every piece.

Press i to hear how much wood you are carrying, press n, e, s, or w to hear a single wall's strength, press t for a quick summary of all four walls, and press d to locate the wood lying around you, nearest first. The P key locates the other players the same way.

When the wave begins, enemies attack your walls with axes, bats, crowbars, and hammers, and you hear each strike at the wall it lands on, louder as that wall weakens. A wall whose strength runs out breaks into rubble you can walk over, and its attackers move to the walls still standing.

The round is lost when all four walls fall; you are then shown your results, the wood you gathered, the rounds you completed, and how long you survived, and asked whether to play again or leave.

Whenever you finish a game having reached a higher round than your best ever, you earn a bonus of twenty to forty starter wood, which is the second way to gain starter wood; it is added on top of your normal starting wood when the next round begins.

Choose play again to stay in the cavern, or leave to return to your room. In an open game with others, the cavern resets for a new round once everyone has answered, and the host begins it from the game menu as before.

Press escape for the pause menu. If you host the game and a round is running, opening it pauses the game for everyone until you resume; a solo game stays paused, while an open game resumes on its own after a minute and a half. Anyone can leave from this menu at any time, and the host can stop the game from it.

Environment versus player.

Environment versus player, or EVP, flips the game around: instead of defending the walls you attack them, and the bots defend. You play from the gravel outside the cave, and your job is to smash all four walls down while the bots build them back up. Choose EVP when you pick your game mode at the start.

You fight with weapons, not wood. When a round starts you are handed all four on the number row: press one for the axe, two for the bat, three for the crowbar, or four for the hammer, and you hear which one you have drawn. Before the round begins you carry nothing and cannot attack.

Walk up to a wall and hold space to swing the weapon in your hand at the nearest wall, the same five tile reach as reinforcing. Each weapon takes a moment to wind up before the blow lands, and heavier weapons hit harder but swing slower, so the hammer does the most damage while the axe lands the fastest. You can keep moving and switch weapons freely while you swing.

The walls are defended by builder bots. They wander the cavern, pick up the wood that drops, carry it to whichever wall is weakest, and repair it, so you hear their footsteps moving around and the wood going onto the walls. You do not gather wood yourself in this mode; the bots do. Press b to hear where the bots are, nearest first, the same way p locates players, and the wall keys n, e, s, w, and t still tell you how the walls are holding up.

Each round has two parts. First a build phase, where the bots reinforce the walls and you cannot hurt them yet; if you swing during this time your weapon only ricochets off the wall, so you know you are lined up, but no damage is done.

Then comes the wave, which alternates between attack windows and rest windows. During an attack window your hits finally count, so smash the walls while you can, and the bots roam the cavern gathering wood but hold off repairing. During a rest window your swings only ricochet again while the bots place that wood and repair the damage, so you cannot hurt the walls until the next attack window opens.

The bots can never rebuild a wall all the way back, though, because part of every hit you land is permanent, so you always gain ground over the round no matter how hard they work.

Each switch is announced, and tab tells you which window you are in. You also have a time limit for the whole wave, which tab reads out as well, but it counts down only during the attack windows, so the rest periods never eat into it; each round you clear adds more time to the next.

Bring every wall down and you clear the round; the cavern is rebuilt and the next round sends more bots to defend it, so it gets harder each time. The game ends when the bots hold you off, that is, when the wave's time runs out with a wall still standing. You are then shown how many rounds you cleared and asked whether to play again or leave. The pause menu works just as it does in the other mode.

Watching games.

You can also watch a game instead of playing it. Choose watch game from the room menu to see every game in the room, including single-player games and games already in progress, and pick one; up to four people can watch a game at once.

You float on a deck above the cavern and roam it freely while the whole battle plays out below you, and the players are told you are watching. You are only an observer, so you carry no wood, cannot reinforce, and the enemies ignore you, but you hear everything and can still chat and use voice with the players.

Most keys work as usual, including tab for the round status, n, e, s, w, and t for the walls, and P to locate the players, while the keys for your own wood and reinforcing do nothing. When you watch an environment versus player game, the deck sits out on the gravel to match, and the b key locates the builder bots as well. Press escape to stop watching and return to the room.

Keyboard commands.

This is the full list of keys CaveDefender uses. Some keys only do something in the right place, for example the wall and weapon keys work only while you are in a game; where that matters it is noted. A few keys do one thing on their own and another with shift held, and both are listed.

Movement.

Left arrow. Step left.
Right arrow. Step right.
Up arrow. Step forward.
Down arrow. Step backward.

Alt. Held while moving, flips between walking and running for as long as you hold it: with auto-running off, holding alt runs; with auto-running on, holding alt walks.
Alt plus letter R. Toggle auto-running on or off, saved between sessions.

Letter, C. Speak your coordinates, the surface you are standing on, and the way you are facing.

Chat.

Slash. Open global chat to type a message or a slash command.
Backslash. Open local chat, heard by everyone in your current space.
Apostrophe. Open staff chat. Staff only.
Semicolon. Open team chat. Only while you are in a game.

Glancing around.

Letter, P. Locate the other players around you, nearest first, by direction and distance.
Letter, R. List who is around: the rooms from the lobby, who is in your room from a room, or who is in the game's room from a game.
Letter, L. List who is in the lobby. Works anywhere, including in a game.
Letter, G. List games: every game on the server from the lobby, the games in your room from a room, or who is in your game from a game.

Server information.

F1. List everyone on the server.
F2. Read the server's message of the day.
F3. Ping the server and hear the round trip time.
F4. Hear how long the server has been running.
F5. Toggle player beacons on or off.
F6. Open the players menu.

Volume.

Page up. Raise the music volume.
Page down. Lower the music volume.
Home. Raise the ambience volume.
End. Lower the ambience volume.

Voice chat.

Letter, O. Talk over voice chat. With hold to talk on, hold O to talk; with it off, press O to start talking and press it again to stop.

The message buffers.

These review past messages, which are sorted into categories such as global chats, private chats, and alerts.

Comma. Move to the previous message in the current category.
Period. Move to the next message in the current category.
Shift plus comma. Jump to the first message in the category.
Shift plus period. Jump to the last message in the category.

Left bracket. Move to the previous category.
Right bracket. Move to the next category.
Shift plus left bracket. Jump to the first category.
Shift plus right bracket. Jump to the last category.

Shift plus letter M. Mute or unmute the current category, so its new messages stop or resume being read aloud.
Shift plus letter C. Copy the current message to the clipboard.
Shift plus backslash. Export the current category to a log file, then clear it.

Menus and leaving.

Enter. Open the menu for where you are: the lobby menu in the lobby, the room menu in a room, or the round menu in a game you host.
Escape. In a game, open the pause menu, or stop watching if you are a spectator. Anywhere else, leave the server and return to the connection menu, asking you to confirm first if that setting is on.

In a game.

These work while you are in a game.

Tab. Hear the current round status.
Letter, N, E, S, or W. Hear the strength of the north, east, south, or west wall.
Letter, T. Hear a summary of all four walls.
Letter, I. Hear how much wood you are carrying. PVE only, and not while watching.
Letter, D. Locate the wood lying around you, nearest first. PVE only, and not while watching.
Shift plus enter. Reinforce the nearest wall in reach with one piece of wood; hold to keep placing. PVE only.
Letter, B. Locate the builder bots, nearest first. EVP only.
Number row, 1, 2, 3, or 4. Draw the axe, bat, crowbar, or hammer. EVP only.
Spacebar. Held, swings your drawn weapon at the nearest wall in reach. EVP only.
