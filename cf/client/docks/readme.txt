Welcome to CaveDefender!

CaveDefender is an online, audio only game. You sign in to an account on a server and share a world with other players: you chat, move around together, make rooms, and play the cave defender game, where you gather wood and defend four walls against waves of enemies, or, in the reverse mode, attack the walls from outside while bots defend them, or, in the player versus player mode, take one side of the walls and fight other players across them, or, in free play, stock your own sandbox cavern and both attack and defend the walls at once. This readme explains how everything works. For the list of typed chat commands, type /help in the game, which opens the player help. For the full list of the keys the game uses, see the keyboard commands section near the end of this readme.

Connecting and signing in.

When you start the game you land on the main menu. Choose the game menu to open the connection menu, where you pick a server and sign in. The other main menu options are the documentation menu, which holds this readme, the changelog, and more, the learn sounds menu described just below, and the preferences menu for your sound and other settings.

Learn sounds.

The main menu also has a learn sounds menu, a place to get familiar with the game's audio before you play. It works offline, so you can browse it without signing in. The sounds are grouped into categories, weapon, wood, ammo, wall, surface, and interface cues; choose a category, then move through its list and press enter on any sound to hear it. Each sound's name tells you where it is used in the game, such as which mode it belongs to, so you learn the cue and its meaning together, and sounds that come in several variations play a random one each time so you can hear how they differ. Choose go back, or press escape, to step out of a category, and again to leave the menu.

The connection menu shows the server address and port it will connect to, and you can change either directly with change server IP and change server port. If you play on more than one server, open Server storage to keep them as presets: add a server by giving it a name, an address, and a port, and edit or remove your saved ones from the same place. Select a server then picks which saved server to use. The list always includes a built-in Central server, the game's official server, ready to pick without your having to add it; you can edit its address or port if you ever need to, but it cannot be removed. At the bottom of the list is a Custom entry that simply keeps whatever address you typed in by hand, so a server you did not save reads as Custom. You cannot save two servers with the same name or the same address.

You reach a server with an account, and there are a few ways on. Sign in as, followed by a name, appears once you have an account set up or selected, and signs you straight in as that account. Set up an existing account remembers an account you already have, by its username and password, so you can sign in as it, without logging you in right away. New account creates a fresh one, asking for a username, an email, a password, and a second password to confirm it; once it is made the game asks whether to log in now.

If you use more than one account on this computer, Account storage keeps them for you: add, edit, or remove your saved accounts there, and Select an account chooses which one is active, the one that Sign in as will use. After you set up or create an account, the game also offers to save it here. As with servers, you cannot save the same account twice.

The server rules.

The first time you sign in you must read the server's rules and agree to them before you can play. Type /rules to read the player rules, then close the page for a quick menu asking whether you agree: yes enters the lobby, no leaves. Everyone must read the player rules to agree; staff must read both the player and staff rules, and may open the staff rules only after reading their own. You only agree once, and are asked again just if the server's rules are later updated. You can reread the rules at any time with /rules, or /rules player and /rules staff to read either page.

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

Any chat box holds more than one line. Press Shift plus Enter, or Control plus Enter, to start a new line while plain Enter still sends, and the up and down arrows move between the lines you have written. This works in every chat box, private messages included, so you can lay out a longer message across several lines.

You can also hear the people around you typing. When someone nearby is writing in a chat box you hear their keyboard from where they stand, so you can tell who is composing a message, and walking away fades it like any other sound; your own typing is heard the same way by others. F3 in any text box turns your own keyboard clicks on or off and also sets whether others hear you, and F4 in any text box turns hearing other people's typing on or off.

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

Choose a player to open a read-only information card about them, showing their username, nickname, pronouns, when they became a member, language channel, rank, whether they are away, where they are, the lobby, a room, or a game, the version of the game they are running, their player versus player win and loss record, their best round in both the cave defender and environment versus player modes, plus the total wood they have collected in the first and the total ammo in the second, and how many warnings they have. Staff also see the player's email and mute status. Press escape or close to leave the card.

The card can also show a Personally mute this player's chats checkbox, with the Alt plus M shortcut, a Personally mute this player's onoffs checkbox, with the Alt plus O shortcut, and a Private message this player button, with Alt plus P, though each appears only when it applies to the player you are viewing, as described below.

Personally muting a player's chats affects only you: while it is on you no longer see their global chat, local chat, or private messages, and you no longer hear their voice, while everyone else still does. The player is not told when you mute them, but if they try to send you a private message they are told they have been muted. They also cannot look up where you are: your location shows as private to them, both with the /where command and on your card. Staff members cannot be muted, so the checkbox does not appear on their card. It stays in effect across sessions until you open their card again and uncheck it, and you can also manage your mutes with the /ignore and /ignored commands. This is separate from the staff silence described below, which quiets a player for everyone rather than only for you.

Personally muting a player's onoffs is a separate mute covering both their sounds and their messages: while it is on, that player's connect and disconnect play the standard cue for you, and their custom online and offline message shows as the standard one too, while everyone else still gets their custom ones. The player is not told, and unlike the chat mute it can be used on anyone, staff included, since it affects only their sounds and messages, not their communication. It stays in effect across sessions until you uncheck it on their card, and you can also manage these mutes with the /ignoreonfs and /ignoredonfs commands.

The private message button asks you for a message and sends it straight to that player, the same as the /pm command. It is hidden if that player has personally muted you, since your message would not reach them. Your own card does not show these controls, since you cannot mute or message yourself.

If you are staff, the card also shows action buttons for the things your rank lets you do to that player: kick, ban, promote, demote, notify, warn, silence, and set their nickname. Only the buttons you are actually allowed to use on that particular player appear, and choosing one asks for anything it needs, such as a ban length, a new rank, a notification, a warning level and reason, the channel to silence and how long, or a new nickname, before carrying out the same action as the matching staff command. Silencing a player is the staff mute that stops everyone hearing them in a channel you choose, which is different from the personal mute above that quiets them only for you; among the channels you can choose is their online and offline sounds, which makes their connect and disconnect standard for everyone, and the same button also lifts a silence you have set. They never let you do anything the commands would not, so all the usual rank rules still apply; the staff help explains each of these in full.

The leaderboard.

Type /lb to open the server-wide leaderboards, which rank every account whether or not that player is currently online. Each game mode has two boards: PVE ranks best round and total wood gathered, while EVP ranks best round and total ammo gathered. With /lb on its own you pick a mode, PVE or EVP, then pick one of its boards from a menu; you can also go straight there by naming the mode in capitals and the board, such as /lb PVE, /lb PVE wood, or /lb EVP ammo, where the board is round, wood, or ammo. Only players with something recorded on a board appear, your own row among them shown just like any other, and choosing a row opens that player's information card if they are online, the same card the players menu opens, or tells you they are offline.

The best round boards count your solo games only. Because everyone in an open game finishes on the same round, that shared number is not truly your own, so a best round counts toward the leaderboard, and earns its milestone bonus, only when you reached it playing alone; open games never change your best round. The total wood and total ammo boards are different: they count every item you personally gather in any real game, solo or open, since what you pick up is always your own even in a crowd. Free play never counts toward any board, being a sandbox where you spawn your own supplies. No two players ever share the same standing: on a best round board a round belongs to whoever reached it first, so if you later match it you do not appear until you push to a further round and pass them, and the gather boards work the same way on your lifetime total. A record's date is not shown; each row is simply the rank, the player, and their best round or total.

Whenever someone climbs to a new place on a leaderboard, everyone on the server is told, for example bob has reached rank 4 on the PVE best round leaderboard. You hear one cue when it is you who moved up and a different one when it is someone else, and only an actual move up is announced, so beating your own record without passing anyone stays quiet. These announcements collect in their own leaderboards message category, which you can review or silence like any other from the message buffers.

The player and location panels.

In the lobby or any room you are in, press enter to open the panel for where you are: the lobby panel in the lobby, or the room panel in a room, which is the create and join rooms menu, or the room menu, both described just below. Press shift plus enter to open the player panel instead, which gathers your personal, account-tied settings in one place: your language channel, your pronoun, your muted players list, and changing your nickname, email, or password, each doing the same as the matching slash command, along with setting your own online and offline sounds, described in its own section below. In a game, enter opens the round menu instead, and your personal settings stay reachable through their slash commands, the players menu on F6, and your preferences on Alt plus P.

Online and offline sounds.

Every player can have their own online and offline sounds. When you connect, everyone on the server hears the sound you chose, and when you disconnect they hear your other one, in place of the standard connect and disconnect cues, so people can tell who is coming and going by ear. If you have not set any, you simply keep the standard cues as before.

To set them, press F7 anywhere in the game, or choose the online and offline sounds option in your player panel. A form opens with a box for each sound: check use online sound and a browse button appears, then browse to any OGG file on your computer and it becomes the sound others hear when you come online, and the offline sound works the same way. Each must be an OGG file no longer than three seconds, so the cues stay short and snappy, and anything too long, too large, or of the wrong type is refused the moment you pick it.

Your chosen sounds are saved to your account on the server. To replace one, browse a new file and save. To remove one, uncheck its use box and save, and you are asked to confirm first, since removing a sound means picking it again if you ever want it back. A separate switch temporarily disables your custom sounds, keeping them saved but falling back to the standard cues until you turn it off; this switch appears only when you have at least one custom sound uploaded and in use, since there is otherwise nothing to disable. A preview button for each sound, always available, lets you hear what will actually play, your saved sound or the standard cue when you have none saved or have your custom sounds disabled. Press escape, or choose cancel changes, to close the form without saving. A server host can also set these sounds for a player who asks.

Whenever anyone changes their online or offline sounds, a short notice arrives in everyone's alerts buffer, your own included, naming the player and saying what they did, whether they updated a sound, removed one, or temporarily muted or unmuted their online and offline sounds, so it is clear when someone's cue is about to sound different.

Online and offline messages.

Alongside your sounds, you can set your own online and offline messages, the words shown after your name when you connect and disconnect. Normally everyone sees your name followed by just came online or just went offline; a custom message replaces those words, so with an online message of has entered the cave, everyone sees your name followed by has entered the cave. Your name is always kept, so people still know who it is.

To set them, type slash onmsg followed by your message, for example slash onmsg has entered the cave, and slash offmsg for your disconnect line. Type slash onmsg default, or slash offmsg default, to go back to the standard wording. You can also set both at once from the change your online and offline messages option in your player panel, which opens a form with a field for each; leave a field blank to use the default. Each message is a single line of up to sixty four characters and is filtered like chat, and only you are told when you change it. Use slash online or slash offline any time to hear your sound and read your message exactly as others will get them.

Soundboard.

You can play a short sound to everyone on the server, chosen from a library the server host keeps on the server. Type slash playsound, or slash pls, followed by the sound's path, for example slash playsound player slash common slash something dot ogg: the first part is the folder and the second is the category, either common or misc. Every player shares the player folder. Type slash playsound on its own, with no path, to open a menu instead, where you choose a folder and then a sound to play, and escape steps back a level or closes the menu once you are as far out as you can go. Whoever plays a sound, everyone on the server hears it the same way wherever they are, and it plays on its own with no message saying who played it. Staff have a staff folder of their own to play from as well, on top of the shared player sounds.

Script keys.

Script keys are your own keyboard shortcuts that run a chat command, or send a message, from anywhere in the game with a single keystroke. They live in a plain text file called scriptkeys dot txt that sits next to the game, which you can open and edit in any text editor. You put one command per line, exactly as you would type it into a chat box, so a line that starts with a slash is a command, such as slash lb, and a line without one is a global chat message. Line one is the first key, line two the second, and so on.

To run a script key, hold Alt and press a key along the number row, the grave key for the first, then 1 through 0, the minus, the equals, and finally backspace for the fourteenth. Holding Alt and Shift together with those same keys runs a second set of fourteen, so there are twenty eight in all. If the line for a key is empty, or the file has no such line, you are told, for example, scriptkey 15 not found.

A line can also ask you for parts of the command as you run it. Anywhere in the line, a percent sign followed by some words is a prompt, and when you press the key the game asks you that question in a box and puts your answer into the command in that spot, asking each prompt in turn from left to right. For example, a line reading slash pm followed by a prompt for who to message and a prompt for what to say asks you both, then sends the private message. Cancelling any prompt, or leaving it blank, cancels the whole command.

The file is read fresh every time you press a script key, so you can edit it while the game is running and your changes work on the very next press, with no need to restart. To send to a channel other than global from a script key, begin the line with one of the channel commands, slash gl for global, slash lc for local, slash st for staff chat, or slash tm for your team, for example slash lc followed by a prompt for a local message.

Rooms.

From the lobby, press enter to open the lobby panel and create or join a public or private room. You can host up to one public and one private room of your own. You hear a sound whenever you join or leave a room, and anyone already in the room hears you come and go too, much like players hear you connect to and leave the server. Joining and leaving rooms share a brief half-second cooldown, so you cannot bounce in and out of a room super fast; it is silent, so a join or leave that comes too soon after your last one is simply ignored until the moment passes.

Inside a room, press enter to open the room panel, the room menu. If you host the room you can use Kick from room to send a player back to the lobby, and, for a private room, set or retrieve its password. The Kick from room list also includes your own name, which you can pick to simply leave your own room, just like Leave room does. You can delete your own room, but only when you are the only one in it and no games are running.

When you join a private room, you are asked for its password first. If you are staff joining a private room you created yourself, that box opens with the password already filled in, so you can just press enter rather than type it; this only happens for your own room, and joining anyone else's private room still asks you to type the password as usual.

Anyone in a room can invite someone to it. Choose Invite to room from the room menu to see everyone currently in the lobby, and pick the person you want. They are told privately that you invited them, and they answer with Alt plus A to accept or Alt plus D to deny; an invitation lasts two minutes before it expires, with a sound playing to let them know when it runs out unanswered, and they can check how long is left with /invtime. Accepting brings them straight in, even past a private room's password, and you are told whether they accepted or declined.

Games.

Inside a room you can start a game, choosing a game mode, then who can play, then a map size, and finally, in this mode, a wall reinforce limit and whether the enemy bots pile onto the remaining walls when one is destroyed, both explained below. Others can join your open games while a game still has room. There are four modes. This section describes the original, player versus environment, or PVE, where you defend four walls that each start at a random strength; the other three, environment versus player, player versus player, and free play, each have their own section below. If you host the game, press enter for the round menu, where you begin the round.

If your game is open, that menu also has Invite to game and Kick from game, which are the same idea as the room's Invite to room and Kick from room but one step further in.

Invite to game first asks where to invite from, your room or the lobby, then lists the players there for you to pick; the player you pick answers the same way, with Alt plus A to accept or Alt plus D to deny. Choosing the lobby pulls someone straight into the cavern, past a private room's password, without their having to join the room first.

A player you invited from the lobby returns to the lobby when they leave the game or it ends, while a player who joined through your room returns to the room; Kick from game follows the same rule, sending each player back to wherever they came from. The Kick from game list also includes your own name, which you can pick to simply leave your own game, the same as leaving through the pause menu.

Anyone can press tab to hear the current round status, such as the build countdown or, once the wave is on, which round it is and whether the enemies are attacking or resting. Each fresh wave is also announced with its round number, for example round one, the enemies are coming, and that number climbs as the round wears on. About ten seconds before each wave, whether the first one at the end of the build phase or a later one after a rest, you get a heads-up sound and an alert telling you how long until the enemies attack.

The round opens with a build phase to prepare, and you begin each round already carrying ten to twenty starter wood so you can shore up a weak wall right away. Wood comes in four kinds, oak, maple, birch, and pine, and your starter wood always arrives as a single random kind, so one round you might open with all pine and another with all oak. More wood drops around the cavern as the round runs, in any of the four kinds, and simply walking near a piece picks up everything within five tiles of you.

Stand within five tiles of any wall and press shift plus enter to spend one piece reinforcing the nearest wall, no matter which way you face. The kinds vary in strength, with pine adding five to ten, birch eight to sixteen, maple twelve to twenty two, and oak fifteen to thirty, and reinforcing spends a random one of the kinds you are carrying, so every kind is worth gathering. How far you can over-build a wall is set when the game is started: its host chooses a reinforce limit of two hundred, four hundred, or eight hundred percent of a wall's full strength, or no limit at all, so up to that cap you can bank as big a buffer as you can gather wood for, and with no limit there is no ceiling. You can reinforce during the build phase and during the rest periods between attacks, but not while the enemies are actively striking. Hold shift plus enter to keep placing wood without pressing it for every piece.

Each piece placed on a wall is heard across the whole length of that wall, so the sound stays with the wall as you move along it and only grows distant as you step away from the wall itself, the same way the wall's other sounds carry. This is true whether it is you reinforcing, another defender, or, in the reverse mode, a builder bot repairing a wall from inside.

Press i to hear how much wood you are carrying, broken down by kind, press n, e, s, or w to hear a single wall's strength, press t for a quick summary of all four walls, and press d to locate the wood lying around you, nearest first, each piece's kind included. The P key locates the other players the same way. These locate keys, along with A for ammo and B for the bots in the modes that use them, give each thing's direction from a fixed north-up view: straight ahead always means north, the way the up arrow moves you, with right being east, behind south, and left west, no matter which way you last walked. This lines up with which ear you hear a sound in, since the game's audio is north-up too.

When the wave begins, enemies attack your walls with axes, bats, crowbars, and hammers, and you hear each strike at the wall it lands on, louder as that wall weakens. A wall whose strength runs out breaks into rubble you can walk over. What becomes of its attackers depends on a choice the host made when starting the game: they either pile onto the walls still standing, so the survivors face more and more enemies as walls fall, or they simply leave the round, so losing a wall eases the pressure instead. Down in the cavern every sound, footsteps, wall hits, wood, and the rest, carries a natural reverb, a soft tail of reflections as in a real enclosed cave; only the open-air areas outside stay dry.

The round is lost when all four walls fall; you are then shown your results, the wood you gathered, the rounds you completed, and how long you survived, and asked whether to play again or leave.

Whenever you finish a solo game having reached a higher round than your best ever, you earn a bonus of twenty to forty starter wood, which is the second way to gain starter wood; like your ordinary starter wood it arrives as a single random kind, and the game over message names the kind you earned, for example thirty two oak. It is added on top of your normal starting wood when the next round begins. This bonus, and your best round record itself, come from solo games only: an open game's round is shared by everyone in it, so it neither sets your best round nor grants this bonus, though the wood you personally gather in an open game still counts toward the leaderboard.

Choose play again to stay in the cavern, or leave to return to your room. In an open game with others, the cavern resets for a new round once everyone has answered, and the host begins it from the game menu as before.

Press escape for the pause menu. If you host the game and a round is running, opening it pauses the game for everyone until you resume; a solo game stays paused, while an open game resumes on its own after a minute and a half. Anyone can leave from this menu at any time, and the host can stop the game from it. While the game is paused, the other players can still use the chat keys and review their message buffers, even though everything else waits for the host to resume.

Environment versus player.

Environment versus player, or EVP, flips the game around: instead of defending the walls, you attack them, and the bots defend. You play from the gravel outside the cave, and your job is to smash all four walls down while the bots build them back up. Choose EVP when you pick your game mode at the start.

You fight with weapons, not wood. When a round starts you are handed all your weapons and one is drawn for you; press Alt plus W at any time to open the weapon menu and pick any of them, with the one you have drawn marked. The menu is arranged in tabs, an All tab that lists every weapon and one tab each for the archery, artillery, explosive, and melee kinds, and it remembers the tab you were last on. The number row works too, drawing the weapons in alphabetical order, the same order as the All tab: 1 through 0 then dash and equals. Before the round begins you carry nothing and cannot attack.

The melee weapons, the axe, bat, crowbar, hammer, and your own fists and feet, are swung up close. Walk up to a wall and press space to swing the one in your hand at the nearest wall, one swing per press, the same five tile reach as reinforcing. Each takes a moment to wind up before the blow lands, and heavier weapons hit harder but swing slower, so the hammer does the most damage while your bare fists land the fastest and hit the softest. You can keep moving and switch weapons freely while you swing.

The ranged weapons, the crossbow, cannon, firebomb, grenade, pistol, and machine gun, are fired from a distance. Face the wall you want to hit and press space to fire; the shot flies across and strikes the wall you are facing from however far back you stand, up to that weapon's range. Ranged shots hit only the walls, never people, so a bullet passes harmlessly through anyone in its path. Each shot spends a round of that weapon's ammo, and pulling the trigger empty just clicks. The machine gun is the one fully automatic weapon: hold space and it keeps firing on its own until you let go or the magazine runs dry.

Ammo is a resource you gather, the attacker's version of the defenders' wood. Several kinds drop on the ground in your area, arrows for the crossbow, powder for the cannon, gas for the firebomb, grenades, and normal ammo shared by the pistol and machine gun, and you pick each up by walking over it. Press x to hear the drawn weapon's ammo, how many rounds are loaded and how many wait in reserve, and press a to locate the nearest ammo on the ground, nearest first, the way d locates wood for the defenders.

Once a weapon is empty, press shift plus R to reload it, moving rounds from your reserve into it. You can only reload an empty weapon, not top up a partly loaded one, so a full magazine is always spent before the next reload. The reload takes as long as its sound plays, blocking you from firing, and from switching to another weapon, until it finishes, so a reload is never thrown away partway through, and a ping tells you the moment it is loaded and ready.

Some weapons set the wall on fire on top of their hit, and the fire keeps gnawing at the wall for a few seconds after. The explosive weapons, the firebomb, cannon, and grenade, light the fiercest and longest fires, while the two heaviest melee weapons, the axe and hammer, leave a smaller, shorter blaze when they land a damaging blow. Hit a wall that is already burning and the fire grows hotter and lasts longer, so a team can stoke a wall down fast. Like your swings, the fire only eats the wall while you can attack it, going quiet during the build phase and the rest windows and picking back up when the next attack window opens. You hear a wall fire spread across the whole length of the wall it burns, so it stays with the wall as you move along it and only grows distant as you step away from the wall itself, the same way the sounds of the wall being struck carry. When a fire goes out, its burning fades down smoothly over about a second as the fire-out sound comes in, rather than cutting off all at once.

The walls are defended by builder bots. They wander the cavern, pick up the wood that drops, carry it to whichever wall is weakest, and repair it, so you hear their footsteps moving around and the wood going onto the walls. Just as your own pieces do, some wood kinds mend a wall more than others when a bot places it. Out on the gravel you hear all of this from outside the walls, so the bots and the cave's wood reach you both muffled and reverberant, as if the inside of the cave is leaking out to you through the stone, while your own sounds on the exterior stay clear. You do not gather wood yourself in this mode; the bots do. Press b to hear where the bots are, nearest first, the same way p locates players, and the wall keys n, e, s, w, and t still tell you how the walls are holding up.

Each round has two parts. First a build phase, where the bots reinforce the walls and you cannot hurt them yet; if you swing or fire during this time your weapon only ricochets off the wall, so you know you are lined up, but no damage is done, and a shot in the build phase spends no ammo.

The wave alternates between attack windows and rest windows. During an attack window your hits finally count, so smash the walls while you can, and the bots roam the cavern gathering wood but hold off repairing. During a rest window your swings and shots only ricochet again, and spend no ammo, while the bots place that wood and repair the damage, so you cannot hurt the walls until the next attack window opens.

The bots can never rebuild a wall all the way back, though, because part of every hit you land is permanent, so you always gain ground over the round no matter how hard they work.

Each switch is announced, and tab tells you which window you are in. You also have a time limit for the whole wave, which tab reads out as well, but it counts down only during the attack windows, so the rest periods never eat into it; each round you clear adds more time to the next.

Bring every wall down and you clear the round; the cavern is rebuilt and the next round is tougher, with the walls fortified higher than before and more bots to defend them, so each round is harder to break than the last and the walls climb well past full strength the further you get. The game ends when the bots hold you off, that is, when the wave's time runs out with a wall still standing. You are then shown how many rounds you cleared and how much ammo you gathered that game, and asked whether to play again or leave. The pause menu works just as it does in the other mode.

Whenever you finish a solo game having cleared more rounds than your best ever, you earn a bonus of ammo for beating your record, a little of every kind added to your reserve when your next game begins. It is the attacker's version of the defenders' bonus starting wood, and the game over screen tells you when you have earned it. Like that wood bonus, this and your EVP best round come from solo games only: an open game's round is shared, so it does not set your best round or grant the bonus, though the ammo you personally gather in an open game still counts toward the leaderboard.

Player versus player.

Player versus player, or PVP, is the wall fight with people on both sides instead of bots. One team attacks the four walls from outside, the other defends them from inside, and nobody ever crosses the walls. Choose PVP when you pick your game mode at the start; it is always an open game.

The map is laid out as a bullseye, not two halves side by side. The defenders hold a square of open floor in the center. Around that center sits the ring of four walls, one on each side, north, east, south, and west, and those walls are the front line. Around the walls, filling the rest of the arena out to an indestructible outer boundary, is the attackers' area. The center and the band around it are sized to give both sides room, so neither is cramped: the defenders hold the interior while the attackers roam the band outside it, the walls standing between them, and neither side can pass through to the other. On a bigger map the whole arena grows, the center and the outer band along with it; the map sizes offered for player versus player are set by the server, so they may differ from the other modes.

Teams are always even: one on one with two players, or two on two with four. You cannot start a lopsided match. When an odd number is waiting, someone can step aside to watch so the rest play even, or you can wait for one more to fill the second pair. Before the round starts each player picks a side from the round menu, attack or defend, and the host can assign anyone's side as well. The host cannot begin until every player is assigned and the two sides are even; if they are not, the game tells you what is missing.

When the host begins, a build phase opens. Each side is taken to its place: the defenders to the center, handed ten to twenty starter wood, and the attackers out to the exterior with a weapon in hand. You are told which side you are on. The defenders gather and shore up the walls while the attackers get into position, but no wall can be hurt yet.

The attack phase begins, and like the reverse mode it alternates between attack windows and build windows, game wide, with the two sides never acting on the walls at the same time. During an attack window the attackers smash the walls with their weapons, exactly as in environment versus player, the same five tile reach, heavier weapons hitting harder but swinging slower, while the defenders can only gather wood, not place it. During a build window the roles flip: the defenders reinforce the walls from the inside, each placed piece adding its wood kind's strength, while the attackers' swings only ricochet and do no damage. Gathering wood off the ground is allowed at any time; only placing it is held to the build windows. Tab tells you which window you are in and reads out the clock, which, as in the reverse mode, counts down only while the attackers can act.

A wall you have battered but not destroyed can still be repaired, up to the reinforce limit the host chose when starting the match, whether that is two hundred, four hundred, or eight hundred percent of a wall's full strength, or no limit at all. A wall smashed all the way to nothing, though, is gone for good: it cannot be rebuilt, and it leaves impassable rubble in its place. That rubble is not a walkable gap, so even with a wall down the attackers still cannot step through into the center; they simply hear the wall they broke as a pile of debris when they bump it. Keeping every wall above zero is the defenders' whole job.

The attackers win by bringing all four walls down. The defenders win by keeping at least one wall standing until the clock runs out. When the match ends, a results screen names the winning side and, for you, how many walls fell or held, along with your own contribution, the damage you dealt as an attacker or the wood you placed as a defender. Every player is then asked whether to play again. Playing again returns everyone to the center to pick sides fresh, and the match waits there until the teams can be filled evenly again; choosing no leaves to your room. Each match you finish also adds to a win and loss record kept on your account, with the whole winning side gaining a win and the whole losing side a loss.

Because the two sides are genuinely separated by the walls, you hear across them as if through stone. Sounds from the far side of the ring, the other team's footsteps and weapon swings, the wood being placed, even their voices, all reach you muffled, while everything on your own side stays clear. The defenders' interior also carries the cave's reverb and its own indoor music, so it rings like the enclosed space it is, while the attackers' exterior stays open and dry, with its own outdoor music, so the two sides even sound like the different places they are.

Team chat, on the semicolon key, lets you talk privately to your own side; see the chat channels section above.

Your keys depend on your side: defenders use the wood and reinforce keys just as in player versus environment, while attackers use the weapon and ammo keys just as in environment versus player. Tab for the round status, the wall keys n, e, s, w, and t, and P to locate the players work for everyone. When you watch a player versus player game you choose whether to observe from the indoor deck above the defenders or the outdoor deck above the attackers, and you press escape to stop watching and return to the room.

Free play.

Free play is a sandbox, a mode with no rounds, no timer, no score, and no winning or losing, meant for practicing, learning the controls, or just messing about. It is the one mode where you both attack and defend at once: every weapon and the wood and reinforce kit are all live together, so you can smash a wall down and then gather wood and build it back up yourself. Choose free play when you pick your game mode, then solo for a private cavern of your own or open to let others join, and a map size. Like the other modes, an open arena needs at least two players before it can begin, while a solo one starts on its own.

You start in an empty cave with the four walls standing at their usual random strengths, but the floor bare, no bots, no wood, and no ammo lying about. You still begin carrying the same starter wood the other modes give, and your starter ammo arrives the first time you draw a ranged weapon, so you are not empty-handed. You stock the cavern and decide when your weapons start to bite through two menus: enter for the state of the arena, and tab for the things in it.

Press enter for the arena menu. Before you have started it offers begin arena, or control plus B, which opens the sandbox for play, and, for the host, change wall reinforce limit, where you set how far wood can reinforce a wall in this arena, the same two hundred, four hundred, or eight hundred percent or no limit choice the other modes ask at the start of a game; free play defaults to no limit, and your choice locks in once you begin the arena.

At first your weapons only ricochet off the walls, a safe setup window while you gather ammo and wood, spawn bots, and get into position; nothing you swing or fire does any damage yet. When you are ready, open the arena menu again and choose enable wall damage, or press control plus B a second time, and your weapons begin to hurt the walls for real. This is a one way switch: once wall damage is on it stays on until you reset the cavern, so there is never any doubt whether your hits are landing. You can pause a running arena too, solo or open: press escape to freeze everything, the attacker bots and the walls' self-healing included, and use the pause menu to resume, leave, or stop, just as in the other modes.

Press tab for the cavern controls, where you populate and clear the sandbox. It opens only once the arena has started, and in an open cavern everyone can use it, not just the host: any player may add attacker bots, builder bots, and items, and clear them, but only the host clears everything at once, resets the whole cavern, or switches on wall damage; a guest clears only a little at a time, as noted below. Spectators watching from a deck cannot open it.

Add cavern attacker bots asks how many you want, up to a hundred at a time, then which wall they attack, north, east, south, west, or all walls. They are the same wall smashers as the other modes, each swinging one of the four melee weapons. If you choose all walls, a third question asks whether to spread that many evenly across the four walls or to put that many on each. Last, you are asked whether these bots should return each time their wall recovers: yes keeps them attacking for good, idling while the wall is down and coming back when it rebuilds, while no lets them leave the moment the wall falls, so you can wear a wall down and have it stay quiet. The bots hammer the walls whether or not your own wall damage is on, so you can set them loose and defend against them.

Add cavern builder bots asks how many builders you want, up to a hundred, and adds that many to the cavern. They are the same wall defenders as in environment versus player: they roam the cave, pick up the wood you have dropped on the floor, and carry it to whichever wall is weakest, mending it up to four times its full strength. Because they build with wood off the ground, you cannot add any until there is wood down for them to pick up, so drop some cavern items first. Press b to locate the builder bots, nearest first, the same way you do in environment versus player.

Add cavern items drops wood, ammo, or both onto the floor for you to gather. You pick which, then the kind, any one wood kind or all wood, any one ammo kind or all ammo, then how many, with the box already filled in with the most that map's floor can hold so you can simply accept it; both simply drops a mix of the two. That maximum depends on the map size, so only the item count box is prefilled, not the attacker or builder bot boxes, whose limit is a flat hundred. Last, you are asked whether these items should spawn continuously: yes keeps that many of them on the floor from then on, dropping fresh ones as you gather them, while no drops them just the once. The pieces scatter across the floor as they do in the other modes, up to the same per-map ground limit, so a small cavern holds fewer than a large one, and a continuous supply is topped up only to that same limit.

Clear cavern attacker bots, clear cavern builder bots, and clear cavern items each show their current count right in the menu as you browse: the attacker bots by how many are on each wall, the builder bots as a plain total, and the items as how much wood and ammo lie on the floor. When the host clears one of these, everything of that kind goes at once; when a guest clears one, they are asked how many and clear only up to that amount, capped at twenty for either kind of bot and five for items, so a guest can help tidy without wiping the host's whole setup.

The guest's how many box starts filled in with the most they can clear, their cap or everything present if there is less, so it is quick to accept. Clearing the cavern items also switches off any continuous item spawning you had running, so cleared items stay gone. Reset cavern map wipes the whole thing, bots, items, and all, rolls the four walls fresh, locks wall damage again, and hands you the axe with empty ammo, as if you had just begun. In an open cavern that reset restores the world for everyone but empties only the host's own weapon and ammo, so a guest keeps what they are carrying.

Modify wall health, which anyone in the cavern can use, sets a chosen wall, or all four at once, straight to a strength you type, one percent of its full strength or higher, as if you had piled on that much wood in an instant. It ignores the reinforce limit, so you can push a wall well past what wood alone would allow, which makes it handy for testing your weapons against a much tougher wall; reset cavern map returns the walls to normal along with everything else.

Any wall you or your bots smash all the way down does not stay broken; it builds itself back up about ten seconds later at a fresh random strength, so there is always something to break. Everyone in the cavern is told the moment a wall goes down and again when it comes back up.

Because both toolkits are live, all the attacker keys and all the defender keys work here at once. Gather wood and reinforce the walls as a defender does in the other modes, and swing or fire your weapons and gather ammo as an attacker does; the wall strength keys, the locate keys, and the rest all behave as they do elsewhere.

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

Shift plus left arrow. Turn to face left without moving, for aiming a weapon in place.
Shift plus right arrow. Turn to face right without moving.
Shift plus up arrow. Turn to face forward without moving.
Shift plus down arrow. Turn to face backward without moving.

Alt. Held while moving, switches between walking and running; which way round depends on your auto-running setting.
Alt plus letter R. Toggle auto-running on or off, saved between sessions.

C. Speak your coordinates, the surface you are standing on, and the way you are facing.

Rooms.

These run lobby or room actions directly without opening the menu first. These first ones work only in the lobby.

Control plus C. Create a public room.
Control plus shift plus C. Create a private room.
Control plus J. Rejoin the last public room you joined or created this session.
Control plus shift plus J. Rejoin the last private room you joined or created this session, with its password already filled in.

These next two answer an invitation and work in the lobby or a room.

Alt plus A. Accept a pending room or game invitation.
Alt plus D. Deny a pending room or game invitation.

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

Control plus B. Begin the round, or in free play begin the arena and then, once it is running, enable wall damage. Host only.
Control plus S. Skip the build phase. Staff host only.
Control plus I. Invite a player to the game. Host of an open game.
Control plus K. Kick a player from the game. Host of an open game.
Control plus C. Choose your side, attack or defend. Player versus player only, before the round starts.
Control plus A. Assign the players to sides. Player versus player host only, before the round starts.
Control plus W. Step aside to watch instead of playing. Player versus player only, before the round starts.

Chat.

Slash. Open global chat.
Backslash. Open local chat.
Apostrophe. Open staff chat. Staff only.
Semicolon. Open team chat, to your own side. Player versus player only.

Text boxes.

These work while you are typing in any text box, such as a chat box.

Shift plus Enter, or Control plus Enter. Start a new line instead of sending; plain Enter still sends, and the up and down arrows then move between your lines.
F2. Cycle how your typing is read back: characters, words, both, or nothing. Saved between sessions.
F3. Turn your own keyboard clicks on or off, which also sets whether nearby players hear you type. Saved.
F4. Turn hearing other players' typing on or off. Saved.

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
F7. Open the form for setting your own online and offline sounds; also reachable from the player panel.

Volume.

Page up. Raise the music volume.
Page down. Lower the music volume.
Home. Raise the ambience volume.
End. Lower the ambience volume.

Voice chat.

O. Talk over voice chat. With hold to talk on, hold O to talk; with it off, press O to start talking and press it again to stop. In preferences, Voice chat mode sets whether your voice streams live as you speak or sends as one recorded message others hear when you finish.

The message buffers.

These review past messages, which are sorted into categories such as global chats, private chats, and alerts. A category only joins the ones you move between once it has a message in it, so cycling skips the empty ones and lands only on categories with something to read; a category you clear drops back out until its next message. The all category, which gathers every message, and the alerts category are always present, since neither can be muted. New messages are still read aloud as they arrive even for a category you are not on, and still collect in all, so hiding an empty category never causes you to miss anything.

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

Enter. In the lobby or a room, open the panel for where you are, the lobby panel or the room panel; in a game you host, open the round menu, or the arena menu in free play.
Shift plus enter. In the lobby or a room, open the player panel, your personal settings in one place.
Alt plus P. Open your preferences without leaving, the same settings you reach from the main menu; saving or canceling returns you to where you were.
Alt plus K. Open the documentation menu without leaving, the changelog, credits, readme, and todo list you also reach from the main menu; closing it returns you to where you were.
Alt plus L. Open the learn sounds menu without leaving, the same sound browser you reach from the main menu; every game sound pauses while it is open so the previews play cleanly, and they all resume the moment you close it. Plain L still lists who is in the lobby.
Shift plus H. Open the help without typing the command; you go straight to the player help, while staff are first asked whether to view the player or the staff help.
Shift plus U. Open the rules without typing the command; you go straight to the player rules, while staff are first asked which page to view.
Escape. In a game, open the pause menu, or stop watching if you are a spectator. Anywhere else, leave the server and return to the connection menu, asking you to confirm first if that setting is on.

In a game.

These work while you are in a game.

Tab. Hear the current round status; in free play, the host opens the cavern controls instead.

N, E, S, or W. Hear the strength of the north, east, south, or west wall.
T. Hear a summary of all four walls.
I. Hear how much wood you are carrying, broken down by kind. For defenders, that is PVE, PVP, and free play; not while watching.
D. Locate the wood lying around you, nearest first, with each piece's kind. For defenders, that is PVE, PVP, and free play; not while watching.

Shift plus enter. Reinforce the nearest wall in reach with one piece of wood; hold to keep placing. Defenders only, in PVE, PVP, and free play.

B. Locate the builder bots, nearest first, in both environment versus player and free play.

Alt plus W. Open the weapon menu to draw any of your weapons, in tabs by kind. For attackers, that is EVP, PVP, and free play.
Number row, 1 through 0 then dash and equals. Draw a weapon directly, in alphabetical order matching the weapon menu's All tab. For attackers, that is EVP, PVP, and free play, the same as Alt plus W.

Spacebar. Swing a drawn melee weapon at the nearest wall, or fire a drawn ranged weapon at the wall you face, once per press; the machine gun instead fires continuously while it is held. For attackers, that is EVP, PVP, and free play.

Shift plus R. Reload the drawn ranged weapon from your reserve once it is empty; a ping sounds when it is loaded, and you cannot switch weapons until the reload finishes, so it is never cut short. For attackers, that is EVP, PVP, and free play.

X. Hear the drawn ranged weapon's ammo, how many rounds are loaded and how many are in reserve. For attackers, that is EVP, PVP, and free play.

A. Locate the ammo lying around you, nearest first, with each one's kind. For attackers, that is EVP, PVP, and free play.

Connection problems.

If your connection drops while you are in a room, a game, or watching one, you are not dropped out of it straight away. The server holds your place for 45 seconds, and the game quietly keeps trying to reconnect the whole time. Get back within that window, which usually happens on its own, and you are put right back where you were, in the same room or game, with your wood, your score, and your host role intact, rather than being dumped in the lobby. To everyone else you simply went offline and then came back. If the game or room ends while you are away, you return to wherever you would have been sent, your room or the lobby; and if you do not make it back in time, or the server itself restarts, you come back to the lobby as usual.

Enjoy, and happy defending!
