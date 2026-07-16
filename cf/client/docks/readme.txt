Welcome to CaveDefender!

CaveDefender is an online, audio only game. You sign in to an account on a server and share a world with other players: you chat, move around together, make rooms, and play the cave defender game, where you gather wood and defend four walls against waves of enemies, or, in the reverse mode, attack the walls from outside while bots defend them, or, in the player versus player mode, take one side of the walls and fight other players across them. This readme explains how everything works. For the list of typed chat commands, type /help in the game, which opens the player help. For the full list of the keys the game uses, see the keyboard commands section near the end of this readme.

Connecting and signing in.

When you start the game you land on the main menu. Choose the game menu to open the connection menu, where you pick a server and sign in. The other main menu options are the documentation menu, which holds this readme, the changelog, and more, and the preferences menu for your sound and other settings.

The connection menu shows the server address and port it will connect to, and you can change either directly with change server IP and change server port. If you play on more than one server, open Server storage to keep them as presets: add a server by giving it a name, an address, and a port, and edit or remove your saved ones from the same place. Select a server then picks which saved server to use, and it opens on a Custom entry that simply keeps whatever address you typed in by hand, so a server you did not save reads as Custom. You cannot save two servers with the same name or the same address.

You reach a server with an account, and there are a few ways on. Sign in as, followed by a name, appears once you have an account set up or selected, and signs you straight in as that account. Set up an existing account remembers an account you already have, by its username and password, so you can sign in as it, without logging you in right away. New account creates a fresh one, asking for a username, an email, a password, and a second password to confirm it; once it is made the game asks whether to log in now.

If you use more than one account on this computer, Account storage keeps them for you: add, edit, or remove your saved accounts there, and Select an account chooses which one is active, the one that Sign in as will use. After you set up or create an account, the game also offers to save it here. As with servers, you cannot save the same account twice.

The server rules.

The first time you sign in you must read the server's rules and agree to them before you can play. Type /rules to read the player rules, then /rules agree to enter the lobby, or /rules disagree to leave. Everyone must read the player rules to agree; staff must read both the player and staff rules, and may open the staff rules only after reading their own. You only agree once, and are asked again just if the server's rules are later updated. You can reread the rules at any time with /rules, or /rules player and /rules staff to read either page.

Moving around.

You move with the arrow keys, and holding alt while you move makes you run. Press alt plus R at any time to toggle auto-running: when it is on you run by default and hold alt to walk instead, and when it is off it works the other way around. The game tells you auto running enabled or disabled as you switch it, and your choice is saved for next time.

Chat channels.

Slash opens global chat, which everyone on the server hears.
Backslash opens local chat, which only the people sharing your current space hear, whether that is the lobby or your room.
Apostrophe opens staff chat, which only staff can send to or hear; as a regular player you can't use it.
Semicolon opens team chat, which reaches only your own side and works only in a player versus player game: attackers hear other attackers, defenders hear other defenders. In the other modes everyone in a game is on one team, so team chat would just repeat local chat, and the semicolon key does nothing there.

Global chat is also divided into language channels. You only hear global messages from people on the same language channel as you, so each language has its own conversation. Local chat, private messages, and staff chat all reach across channels, so local chat reaches everyone sharing your space whatever channel they are on. Choose your language with /channel, everyone starts on English, and your choice is saved for next time.

One of the channels is named Unfiltered. It works like any other channel, in that you only hear global chat from people who have also chosen it, but it is the one channel where the word filter is switched off for global chat. Unfiltered is meant for talking freely, including adult or NSFW topics, so pick it only if you are happy to both read and write that kind of language. No one is ever put there automatically, and you can leave it any time by choosing another channel with /channel.

You can run any command from any chat you have access to.

Chat filtering.

Chat is filtered for forbidden words, a list set by the server's host. If a message you send contains one it is not delivered to anyone, and you are told that it contains forbidden words. Global chat skips this word filter only on the Unfiltered language channel; local chat is always filtered no matter your channel, and staff chat is not word filtered.

Separately, there is always-on protection against screen reader crash strings: character sequences that can crash text to speech engines such as Eloquence or IBMTTS when spoken aloud. This protection covers every chat channel, including Unfiltered, local, and staff, and cannot be turned off, so no one can crash other players' speech by sending one in chat.

Anti-spam.

Global chat has an anti-spam guard that keeps one person from flooding the channel. If you send too many global messages too quickly, the server automatically mutes your global chat for a set time, just like any timed mute: you are told it has happened, and it lifts on its own once the time is up. The guard watches global chat in particular because that is where the language channels live, so keeping it readable matters most there; local, team, and staff chat are not covered.

How many messages count as spamming, how close together they have to arrive, and how long the mute lasts are all set by the server's host, who can also switch the guard off entirely. Staff are never affected by it. Once your mute lifts you begin with a clean slate, so a single quick message afterwards will not trip it again.

Pronouns.

Messages that talk about you in the third person can use your pronouns, for example when you raise your staff flag, change your nickname, or join a room. Choose them with /pronoun, which opens a menu of the options the server offers, such as masculine, feminine, singular they, or one of several neopronoun sets. Everyone starts on singular they, and your choice is saved for next time. There is also a none option, which simply uses your name in place of a pronoun, so the message reads with your name rather than he, she, or they.

The players menu.

Press F6 anywhere to open the players menu, a list of everyone on the server shown by their away status, rank, name, and current language channel, the same people the /who command reads out.

Choose a player to open a read-only information card about them, showing their username, nickname, pronouns, when they became a member, language channel, rank, whether they are away, where they are, the lobby, a room, or a game, the version of the game they are running, their player versus player win and loss record, their best round in both the cave defender and environment versus player modes, and how many warnings they have. Staff also see the player's email and mute status. Press escape or close to leave the card.

The card can also show a Mute this player checkbox, with the Alt plus M shortcut, and a Private message this player button, with Alt plus P, though each appears only when it applies to the player you are viewing, as described below.

Muting a player is personal and affects only you: while it is on you no longer see their global chat, local chat, or private messages, and you no longer hear their voice, while everyone else still does. The player is not told when you mute them, but if they try to send you a private message they are told they have been muted. They also cannot look up where you are: your location shows as private to them, both with the /where command and on your card. Staff members cannot be muted, so the checkbox does not appear on their card. It stays in effect across sessions until you open their card again and uncheck it, and you can also manage your mutes with the /ignore and /ignored commands.

The private message button asks you for a message and sends it straight to that player, the same as the /pm command. It is hidden if that player has personally muted you, since your message would not reach them. Your own card does not show either control, since you cannot mute or message yourself.

If you are staff, the card also shows action buttons for the things your rank lets you do to that player: kick, ban, promote, demote, notify, and warn. Only the buttons you are actually allowed to use on that particular player appear, and choosing one asks for anything it needs, such as a ban length, a new rank, a notification, or a warning level and reason, before carrying out the same action as the matching staff command. They never let you do anything the commands would not, so all the usual rank rules still apply; the staff help explains each of these in full.

The actions menu.

In the lobby or any room you are in, press enter to open the actions menu. It has two items. The account panel gathers your personal, account-tied settings in one place: your language channel, your pronoun, your muted players list, and changing your nickname, email, or password, each doing the same as the matching slash command. The lobby panel, called the room panel when you are in a room, is the create and join rooms menu, or the room menu, both described just below. In a game, enter opens the round menu instead, and your personal settings stay reachable through their slash commands, the players menu on F6, and your preferences on Alt plus P. You can also jump straight to a panel without the actions menu: control plus A opens the account panel, and control plus H opens the lobby or room panel for wherever you are.

Rooms.

From the lobby, press enter and choose the lobby panel to create or join a public or private room. You can host up to one public and one private room of your own.

Inside a room, press enter and choose the room panel for the room menu. If you host the room you can use Kick from room to send a player back to the lobby, and, for a private room, set or retrieve its password. The Kick from room list also includes your own name, which you can pick to simply leave your own room, just like Leave room does. You can delete your own room, but only when you are the only one in it and no games are running.

When you join a private room, you are asked for its password first. If you are staff joining a private room you created yourself, that box opens with the password already filled in, so you can just press enter rather than type it; this only happens for your own room, and joining anyone else's private room still asks you to type the password as usual.

Anyone in a room can invite someone to it. Choose Invite to room from the room menu to see everyone currently in the lobby, and pick the person you want. They are told privately that you invited them, and they join by typing /accept, or refuse with /reject; an invitation lasts two minutes before it expires. Accepting brings them straight in, even past a private room's password, and you are told whether they accepted or declined.

Games.

Inside a room you can start a game, choosing a game mode, then who can play, then a map size, and finally, in this mode, a wall reinforce limit and whether the enemy bots pile onto the remaining walls when one is destroyed, both explained below. Others can join your open games while a game still has room. There are three modes. This section describes the original, player versus environment, or PVE, where you defend four walls that each start at a random strength; the other two, environment versus player and player versus player, each have their own section below. If you host the game, press enter for the round menu, where you begin the round.

If your game is open, that menu also has Invite to game and Kick from game, which are the same idea as the room's Invite to room and Kick from room but one step further in.

Invite to game first asks where to invite from, your room or the lobby, then lists the players there for you to pick; the player you pick answers the same way, with /accept or /reject. Choosing the lobby pulls someone straight into the cavern, past a private room's password, without their having to join the room first.

A player you invited from the lobby returns to the lobby when they leave the game or it ends, while a player who joined through your room returns to the room; Kick from game follows the same rule, sending each player back to wherever they came from. The Kick from game list also includes your own name, which you can pick to simply leave your own game, the same as leaving through the pause menu.

Anyone can press tab to hear the current round status, such as the build countdown or, once the wave is on, which round it is and whether the enemies are attacking or resting. Each fresh wave is also announced with its round number, for example round one, the enemies are coming, and that number climbs as the round wears on. About ten seconds before each wave, whether the first one at the end of the build phase or a later one after a rest, you get a heads-up sound and an alert telling you how long until the enemies attack.

The round opens with a build phase to prepare, and you begin each round already carrying ten to twenty starter wood so you can shore up a weak wall right away. Wood comes in four kinds, oak, maple, birch, and pine, and your starter wood always arrives as a single random kind, so one round you might open with all pine and another with all oak. More wood drops around the cavern as the round runs, in any of the four kinds, and simply walking near a piece picks up everything within five tiles of you.

Stand within five tiles of any wall and press shift plus enter to spend one piece reinforcing the nearest wall, no matter which way you face. The kinds vary in strength, with pine adding five to ten, birch eight to sixteen, maple twelve to twenty two, and oak fifteen to thirty, and reinforcing spends a random one of the kinds you are carrying, so every kind is worth gathering. How far you can over-build a wall is set when the game is started: its host chooses a reinforce limit of two hundred, four hundred, or eight hundred percent of a wall's full strength, or no limit at all, so up to that cap you can bank as big a buffer as you can gather wood for, and with no limit there is no ceiling. You can reinforce during the build phase and during the rest periods between attacks, but not while the enemies are actively striking. Hold shift plus enter to keep placing wood without pressing it for every piece.

Press i to hear how much wood you are carrying, broken down by kind, press n, e, s, or w to hear a single wall's strength, press t for a quick summary of all four walls, and press d to locate the wood lying around you, nearest first, each piece's kind included. The P key locates the other players the same way.

When the wave begins, enemies attack your walls with axes, bats, crowbars, and hammers, and you hear each strike at the wall it lands on, louder as that wall weakens. A wall whose strength runs out breaks into rubble you can walk over. What becomes of its attackers depends on a choice the host made when starting the game: they either pile onto the walls still standing, so the survivors face more and more enemies as walls fall, or they simply leave the round, so losing a wall eases the pressure instead. Down in the cavern every sound, footsteps, wall hits, wood, and the rest, carries a natural reverb, a soft tail of reflections as in a real enclosed cave; only the open-air areas outside stay dry.

The round is lost when all four walls fall; you are then shown your results, the wood you gathered, the rounds you completed, and how long you survived, and asked whether to play again or leave.

Whenever you finish a game having reached a higher round than your best ever, you earn a bonus of twenty to forty starter wood, which is the second way to gain starter wood; like your ordinary starter wood it arrives as a single random kind, and the game over message names the kind you earned, for example thirty two oak. It is added on top of your normal starting wood when the next round begins.

Choose play again to stay in the cavern, or leave to return to your room. In an open game with others, the cavern resets for a new round once everyone has answered, and the host begins it from the game menu as before.

Press escape for the pause menu. If you host the game and a round is running, opening it pauses the game for everyone until you resume; a solo game stays paused, while an open game resumes on its own after a minute and a half. Anyone can leave from this menu at any time, and the host can stop the game from it. While the game is paused, the other players can still use the chat keys and review their message buffers, even though everything else waits for the host to resume.

Environment versus player.

Environment versus player, or EVP, flips the game around: instead of defending the walls, you attack them, and the bots defend. You play from the gravel outside the cave, and your job is to smash all four walls down while the bots build them back up. Choose EVP when you pick your game mode at the start.

You fight with weapons, not wood. When a round starts you are handed all your weapons and one is drawn for you; press Alt plus W at any time to open the weapon menu and pick any of them, with the one you have drawn marked. The menu is arranged in tabs, an All tab that lists every weapon and one tab each for the archery, artillery, explosive, and melee kinds, and it remembers the tab you were last on. Before the round begins you carry nothing and cannot attack.

The melee weapons, the axe, bat, crowbar, hammer, and your own fists and feet, are swung up close. Walk up to a wall and press space to swing the one in your hand at the nearest wall, one swing per press, the same five tile reach as reinforcing. Each takes a moment to wind up before the blow lands, and heavier weapons hit harder but swing slower, so the hammer does the most damage while your bare fists land the fastest and hit the softest. You can keep moving and switch weapons freely while you swing.

The ranged weapons, the crossbow, cannon, firebomb, grenade, pistol, and machine gun, are fired from a distance. Face the wall you want to hit and press space to fire; the shot flies across and strikes the wall you are facing from however far back you stand, up to that weapon's range. Ranged shots hit only the walls, never people, so a bullet passes harmlessly through anyone in its path. Each shot spends a round of that weapon's ammo, and pulling the trigger empty just clicks. The machine gun is the one fully automatic weapon: hold space and it keeps firing on its own until you let go or the magazine runs dry.

Ammo is a resource you gather, the attacker's version of the defenders' wood. Several kinds drop on the ground in your area, arrows for the crossbow, powder for the cannon, gas for the firebomb, grenades, and normal ammo shared by the pistol and machine gun, and you pick each up by walking over it. Press x to hear the drawn weapon's ammo, how many rounds are loaded and how many wait in reserve, and press a to locate the nearest ammo on the ground, nearest first, the way d locates wood for the defenders.

When a weapon runs low, press shift plus R to reload it, moving rounds from your reserve into it. The reload takes as long as its sound plays, blocking you from firing until it finishes, and a ping tells you the moment it is loaded and ready.

The firebomb is special: on top of its hit, it sets the wall alight, and the fire keeps gnawing at the wall for a few seconds. Throw another at a wall already burning and the fire grows hotter and lasts longer. Like your swings, the fire only eats the wall while you can actually attack it, going quiet during the build phase and the rest windows and picking back up when the next attack window opens.

The walls are defended by builder bots. They wander the cavern, pick up the wood that drops, carry it to whichever wall is weakest, and repair it, so you hear their footsteps moving around and the wood going onto the walls. Just as your own pieces do, some wood kinds mend a wall more than others when a bot places it. Out on the gravel you hear all of this from outside the walls, so the bots and the cave's wood reach you both muffled and reverberant, as if the inside of the cave is leaking out to you through the stone, while your own sounds on the exterior stay clear. You do not gather wood yourself in this mode; the bots do. Press b to hear where the bots are, nearest first, the same way p locates players, and the wall keys n, e, s, w, and t still tell you how the walls are holding up.

Each round has two parts. First a build phase, where the bots reinforce the walls and you cannot hurt them yet; if you swing or fire during this time your weapon only ricochets off the wall, so you know you are lined up, but no damage is done, and a shot in the build phase spends no ammo.

The wave alternates between attack windows and rest windows. During an attack window your hits finally count, so smash the walls while you can, and the bots roam the cavern gathering wood but hold off repairing. During a rest window your swings and shots only ricochet again, and spend no ammo, while the bots place that wood and repair the damage, so you cannot hurt the walls until the next attack window opens.

The bots can never rebuild a wall all the way back, though, because part of every hit you land is permanent, so you always gain ground over the round no matter how hard they work.

Each switch is announced, and tab tells you which window you are in. You also have a time limit for the whole wave, which tab reads out as well, but it counts down only during the attack windows, so the rest periods never eat into it; each round you clear adds more time to the next.

Bring every wall down and you clear the round; the cavern is rebuilt and the next round sends more bots to defend it, so it gets harder each time. The game ends when the bots hold you off, that is, when the wave's time runs out with a wall still standing. You are then shown how many rounds you cleared and asked whether to play again or leave. The pause menu works just as it does in the other mode.

Player versus player.

Player versus player, or PVP, is the wall fight with people on both sides instead of bots. One team attacks the four walls from outside, the other defends them from inside, and nobody ever crosses the walls. Choose PVP when you pick your game mode at the start; it is always an open game.

The map is laid out as a bullseye, not two halves side by side. The defenders hold a square of open floor in the very center. Around that center sits the ring of four walls, one on each side, north, east, south, and west, and those walls are the front line. Around the walls, filling the rest of the arena out to an indestructible outer boundary, is the attackers' area. So the defenders are penned inside the ring while the attackers roam the band outside it; the walls stand between them, and neither side can pass through to the other. On a bigger map the whole arena grows, the center square and the outer band along with it.

Teams are always even: one on one with two players, or two on two with four. You cannot start a lopsided match. When an odd number is waiting, someone can step aside to watch so the rest play even, or you can wait for one more to fill the second pair. Before the round starts each player picks a side from the round menu, attack or defend, and the host can assign anyone's side as well. The host cannot begin until every player is assigned and the two sides are even; if they are not, the game tells you what is missing.

When the host begins, a build phase opens. Each side is taken to its place: the defenders to the center, handed ten to twenty starter wood, and the attackers out to the exterior with a weapon in hand. You are told which side you are on. The defenders gather and shore up the walls while the attackers get into position, but no wall can be hurt yet.

The attack phase begins, and like the reverse mode it alternates between attack windows and build windows, game wide, with the two sides never acting on the walls at the same time. During an attack window the attackers smash the walls with their weapons, exactly as in environment versus player, the same five tile reach, heavier weapons hitting harder but swinging slower, while the defenders can only gather wood, not place it. During a build window the roles flip: the defenders reinforce the walls from the inside, each placed piece adding its wood kind's strength, while the attackers' swings only ricochet and do no damage. Gathering wood off the ground is allowed at any time; only placing it is held to the build windows. Tab tells you which window you are in and reads out the clock, which, as in the reverse mode, counts down only while the attackers can act.

A wall you have battered but not destroyed can still be repaired, up to the reinforce limit the host chose when starting the match, whether that is two hundred, four hundred, or eight hundred percent of a wall's full strength, or no limit at all. A wall smashed all the way to nothing, though, is gone for good: it cannot be rebuilt, and it leaves impassable rubble in its place. That rubble is not a walkable gap, so even with a wall down the attackers still cannot step through into the center; they simply hear the wall they broke as a pile of debris when they bump it. Keeping every wall above zero is the defenders' whole job.

The attackers win by bringing all four walls down. The defenders win by keeping at least one wall standing until the clock runs out. When the match ends, a results screen names the winning side and, for you, how many walls fell or held, along with your own contribution, the damage you dealt as an attacker or the wood you placed as a defender. Every player is then asked whether to play again. Playing again returns everyone to the center to pick sides fresh, and the match waits there until the teams can be filled evenly again; choosing no leaves to your room. Each match you finish also adds to a win and loss record kept on your account, with the whole winning side gaining a win and the whole losing side a loss.

Because the two sides are genuinely separated by the walls, you hear across them as if through stone. Sounds from the far side of the ring, the other team's footsteps and weapon swings, the wood being placed, even their voices, all reach you muffled, while everything on your own side stays clear. The defenders' interior also carries the cave's reverb, so it rings like the enclosed space it is, while the attackers' exterior stays open and dry.

Team chat, on the semicolon key, lets you talk privately to your own side; see the chat channels section above.

Watching games.

You can also watch a game instead of playing it. Choose watch game from the room menu to see every game in the room, including single-player games and games already in progress, and pick one; up to four people can watch a game at once.

You float on a deck above the cavern and roam it freely while the whole battle plays out below you, and the players are told you are watching. You are only an observer, so you carry no wood, cannot reinforce, and the enemies ignore you, but you hear everything and can still chat and use voice with the players.

Most keys work as usual, including tab for the round status, n, e, s, w, and t for the walls, and P to locate the players, while the keys for your own wood and reinforcing do nothing. When you watch an environment versus player game, the deck sits out on the gravel to match, and the b key locates the builder bots as well. When you watch a player versus player game, you choose whether to observe from the indoor deck above the defenders or the outdoor deck above the attackers. Press escape to stop watching and return to the room.

Keyboard commands.

This is the full list of keys CaveDefender uses. Some keys only do something in the right place, for example the wall and weapon keys work only while you are in a game; where that matters it is noted. A few keys do one thing on their own and another with shift held, and both are listed.

Movement.

Left arrow. Step left.
Right arrow. Step right.
Up arrow. Step forward.
Down arrow. Step backward.

Alt. Held while moving, switches between walking and running; which way round depends on your auto-running setting.
Alt plus letter R. Toggle auto-running on or off, saved between sessions.

C. Speak your coordinates, the surface you are standing on, and the way you are facing.

Rooms.

Control plus A. Open the account panel. Works in the lobby and any room.
Control plus H. Open the panel for where you are: the lobby panel in the lobby, or the room panel in a room.

The rest of these run lobby or room actions directly without opening the menu first. These first ones work only in the lobby.

Control plus C. Create a public room.
Control plus shift plus C. Create a private room.
Control plus J. Rejoin the last public room you joined this session.
Control plus shift plus J. Rejoin the last private room you joined this session, with its password already filled in.

While inside a room, these run the room menu's actions without opening it first.

Control plus S. Start a game.
Control plus shift plus S. Stop a game.
Control plus J. Join a game.
Control plus W. Watch a game.
Control plus I. Invite a player to the room.
Control plus K. Kick a player from the room.
Control plus P. Set the room's password. Private rooms only.
Control plus R. Retrieve the room's password. Private rooms only.
Control plus D. Delete the room.
Control plus L. Leave the room.

Round menu shortcuts. These run the round menu's actions without opening it, and only do something when the action is actually available to you. Every menu that has these shortcuts, the lobby, room, and round menus, also shows each item's shortcut beside it, so you can learn them by opening the menu too. Once you know the keys, you can hide these labels by turning off Read keyboard shortcuts in menus on the Menu tab of preferences.

Control plus B. Begin the round. Host only.
Control plus S. Skip the build phase. Staff host only.
Control plus I. Invite a player to the game. Host of an open game.
Control plus K. Kick a player from the game. Host of an open game.
Control plus C. Choose your side. Player versus player only.
Control plus A. Assign players to sides. Player versus player host only.
Control plus W. Watch instead. Player versus player only.

Chat.

Slash. Open global chat.
Backslash. Open local chat.
Apostrophe. Open staff chat. Staff only.
Semicolon. Open team chat. Player versus player only.

Glancing around.

P. Locate the other players around you, nearest first, by direction and distance.
R. List who is around: the rooms from the lobby, who is in your room from a room, or who is in the game's room from a game.
L. List who is in the lobby. Works anywhere, including in a game.
G. List games: every game on the server from the lobby, the games in your room from a room, or who is in your game from a game.

Server information.

F1. List everyone on the server.
F2. Read the server's message of the day.
F3. Ping the server and hear the round trip time.
F4. Hear how long the server has been running, and the most players ever connected at once.
F5. Toggle player beacons on or off.
F6. Open the players menu.

Volume.

Page up. Raise the music volume.
Page down. Lower the music volume.
Home. Raise the ambience volume.
End. Lower the ambience volume.

Voice chat.

O. Talk over voice chat. With hold to talk on, hold O to talk; with it off, press O to start talking and press it again to stop.

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

Shift plus M. Mute or unmute the current category, so its new messages stop or resume being read aloud.
Shift plus C. Copy the current message to the clipboard.
Alt plus shift plus C. Open the current message in a read-only box you can read at your own pace with the arrow keys, with a close button to leave it.
Shift plus backslash. Export the current category to a log file, then clear it.
Shift plus B. Open the Buffer menu, which gathers everything you can do with the current category into one list: copy, export, or review the whole category or just the message you are on, and mute or unmute the category.

Menus and leaving.

Enter. In the lobby or a room, open the actions menu, with its account panel and the lobby or room panel; in a game you host, open the round menu.
Alt plus P. Open your preferences without leaving, the same settings you reach from the main menu; saving or canceling returns you to where you were.
Escape. In a game, open the pause menu, or stop watching if you are a spectator. Anywhere else, leave the server and return to the connection menu, asking you to confirm first if that setting is on.

In a game.

These work while you are in a game.

Tab. Hear the current round status.

N, E, S, or W. Hear the strength of the north, east, south, or west wall.
T. Hear a summary of all four walls.
I. Hear how much wood you are carrying, broken down by kind. For defenders, that is PVE and PVP; not while watching.
D. Locate the wood lying around you, nearest first, with each piece's kind. For defenders, that is PVE and PVP; not while watching.

Shift plus enter. Reinforce the nearest wall in reach with one piece of wood; hold to keep placing. Defenders only, in PVE and PVP.

B. Locate the builder bots, nearest first. EVP only.

Alt plus W. Open the weapon menu to draw any of your weapons, in tabs by kind. For attackers, that is EVP and PVP.

Spacebar. Swing a drawn melee weapon at the nearest wall, or fire a drawn ranged weapon at the wall you face, once per press; the machine gun instead fires continuously while it is held. For attackers, that is EVP and PVP.

Shift plus R. Reload the drawn ranged weapon from your reserve; a ping sounds when it is loaded. For attackers, that is EVP and PVP.

X. Hear the drawn ranged weapon's ammo, how many rounds are loaded and how many are in reserve. For attackers, that is EVP and PVP.

A. Locate the ammo lying around you, nearest first, with each one's kind. For attackers, that is EVP and PVP.

Connection problems.

If your connection drops while you are in a room, a game, or watching one, you are not dropped out of it straight away. The server holds your place for 45 seconds, and the game quietly keeps trying to reconnect the whole time. Get back within that window, which usually happens on its own, and you are put right back where you were, in the same room or game, with your wood, your score, and your host role intact, rather than being dumped in the lobby. To everyone else you simply went offline and then came back. If the game or room ends while you are away, you return to wherever you would have been sent, your room or the lobby; and if you do not make it back in time, or the server itself restarts, you come back to the lobby as usual.

Enjoy, and happy defending!
