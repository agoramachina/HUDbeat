
/* Keyboard Shortcuts */
/*
* evaluate: ctrl + enter
* stop: ctrl + .
 * clean Post window: ctrl + shift + P
*/


"Hello World".postln;

{SinOsc.ar}.play;
{SinOsc.ar(LFNoise0.kr(10).range(500, 1500), mul: 0.1)}.play;
{RLPF.ar(Dust.ar([12, 15]), LFNoise1.ar([0.3, 0.2]).range(100, 3000), 0.02)}.play;


// Pitch
// PLAY A4
Pbind(\degree, 5).play;
Pbind(\note, 9).play;
Pbind(\midinote, 69).play;
Pbind(\freq, 440).play;


// Pseq, Pseries, Pbind
Pbind(\degree, Pseries(0, 1, 30), \dur, 0.05).play;
Pbind(\degree, 0).play;
Pbind(\degree, Pseq([0, 1, 2, 3, 4, 5, 6, 7], 1), \dur, 0.2).play;
Pbind(\degree, Pseq([0, 1, 2, 3, 4, 5, 6, 7], 5), \dur, Pseq([0.2, 0.1, 0.1, 0.2, 0.2, 0.35], inf)).play;

(
// Prand
Pbind(
\degree, Prand([2, 3, 4, 5, 6], inf),
\dur, 0.15,
\amp, 0.2,
\legato, 0.1
).play;
)

// Pwhite
(
Pbind(
\freq, Pwhite(100, 500),
\dur, Prand([0.15, 0.25, 0.3], inf),
\amp, 0.2,
\legato, 0.3
).trace.play //DEBUG
)


// Chords
(
Pbind(
\note, Pseq([[0, 3, 7], [2, 5, 8], [3, 7, 10], [5, 8, 12]], 3),
\dur, 0.15
).play;
)

// Fun with strum
(
Pbind(
 \note, Pseq([[−7, 3, 7, 10], [0, 3, 5, 8]], 2),
 \dur, 1,
 \legato, 0.4,
 \strum, 0.1 // try 0, 0.1, 0.2, etc
 ).play;
 )

// Scales
Scale.directory;

(
Pbind (
	\scale, Scale.harmonicMinor,
	\degree, Pseq([0, 1, 2, 3, 4, 5, 6, 7], 1),
	\dur, 0.15;
).play;
)

(
Pbind (
	\degree, Pseq([0, 1, 2, 3, 3.1, 4], 1),
).play;
)

// Transposition
(
Pbind(
\note, Pser([0, 2, 3, 5, 7, 8, 11, 12], 11),
\ctranspose, 12, // transpose an octave above (= 12 semitones)
\dur, 0.15;
).play;
)

// Microtones
// Microtones with \note and \midinote:
(
Pbind(\note, Pseq([0, 0.5, 1, 1.5, 1.75, 2], 1)).play;
Pbind(\midinote, Pseq([60, 69, 68.5, 60.25, 70], 1)).play;
)

// Tempo
(
Pbind(\degree, Pseq([0, 0.1, 1, 2, 3, 4, 5, 6, 7]),
\dur, 1;
).play(TempoClock(120/60)); // 120 beats over 60 seconds: 120 BPM
)

// Rests
(
Pbind(
\degree, Pwhite(0, 10),
\dur, Pseq([0.1, 0.1, 0.3, 0.6, Rest(0.3), 0.25], inf);
).play;
)

// Amplitude and Legato
(
Pbind(
\degree, Pseq([0, −1, 2, −3, 4, −3, 7, 11, 4, 2, 0, −3], 5),
\dur, Pseq([0.2, 0.1, 0.1], inf),
\amp, Pseq([0.7, 0.5, 0.3, 0.2], inf),
\legato, 0.4
).play;
)

// Score
// Define the score
(
p = Pbind(
\midinote, Pseq([57, 62, 64, 65, 67, 69], inf),
\dur, 1/7
); // no .play here!
)
// Ask for the score to be played
 p.play;

// modulate a sine frequency and a noise amplitude with another sine
// whose frequency depends on the horizontal mouse pointer position

{SinOsc.ar(freq: MouseX.kr(300, 2500), mul: MouseY.kr(0, 1))}.play;
({
        var x = SinOsc.ar(MouseX.kr(1, 100));
        SinOsc.ar(300 * x + 800, 0, 0.1)
        +
        PinkNoise.ar(0.1 * x + 0.1)
}.play;
)

{ SinOsc.ar }.plot; // sine wave
{ Saw.ar }.plot; // sawtooth wave
{ Pulse.ar }.plot; // square wave


// Microphone
// Warning: use headphones to avoid feedback
{SoundIn.ar(0)}.play; // same as In.ar(8): takes sound from the first input bus
// Stereo version
{SoundIn.ar([0, 1])}.play; // first and second inputs
// Some reverb just for fun?
{FreeVerb.ar(SoundIn.ar([0, 1]), mix: 0.5, room: 0.9)}.play;

// Multichannel
{Out.ar(0, Saw.ar(freq: [440, 570], mul: Line.kr(0, 1, 10)))}.play;

a = {Out.ar(0, SinOsc.ar(freq: [800, 880], mul: LFPulse.ar(2)))}.play;
a.free;

// Panning
p = {Pan2.ar(in: PinkNoise.ar, pos: SinOsc.kr(2), level: 0.1)}.play;
p.free;

// Synth Nodes
s.plotTree;
 // run these one by one (don't stop the sound) and watch the Node Tree:
w = { SinOsc.ar(60.midicps, 0, 0.1) }.play;
x = { SinOsc.ar(64.midicps, 0, 0.1) }.play;
y = { SinOsc.ar(67.midicps, 0, 0.1) }.play;
z = { SinOsc.ar(71.midicps, 0, 0.1) }.play;
w.free;
x.free;
y.free;
z.free;

// Arrays
// Create some array
a = [10, 11, 12, 13, 14, 15, 16, 17];
a.reverse; // reverse
a.scramble; // scramble
a.choose; // picks one element at random
a.size; // returns size of array
a.at(0); // retrieves item at specified position
a[0] ; // same as above
a.wrapAt(9); // retrieves item at specified position, wrapping around if > a.size
["wow", 99] ++ a; // concatenates the two arrays into a new one
a ++ \hi; // a Symbol is a single character
a ++ 'hi'; // same as above
a ++ "hi"; // a String is a collection of characters
a.add(44); // creates new array with new element at the end
a.insert(5, "wow"); // inserts "wow" at position 5, pushes other items forward (returns new array)
a; // evaluate this and see that none of the above operations actually changed the original array
a.put(2, "oops"); // put "oops" at index 2 (destructive; evaluate line above again to check)
a.permute(3); // permute: item in position 3 goes to position 0, and vice−versa
a.mirror; // makes it a palindrome
a.powerset; // returns all possible combinations of the array's elements

// EventStreamPlayer
~myPlayer = p.play;
~myPlayer.stop;
~myPlayer.resume;
~myPlayer.stop.reset;
~myPlayer.start;
~myPlayer.stop;

// if/else
if(100 > 50, { "very true".postln }, { "very false".postln });

// MIDI
// Quick way to connect all available devices to SC
MIDIIn.connectAll;
// Quick way to see all incoming MIDI messages
MIDIFunc.trace(true);
MIDIFunc.trace(false); // stop it
// Quick way to inspect all CC inputs
MIDIdef.cc(\someCC, {arg a, b; [a, b].postln});

// Get input only from cc 7, channel 0
MIDIdef.cc(\someSpecificControl, {arg a, b; [a, b].postln}, ccNum: 7, chan: 0);

// A SynthDef for quick tests
SynthDef("quick", {arg freq, amp; Out.ar(0, SinOsc.ar(freq) * Env.perc(level: amp).kr(2))}).add;
// Play from a keyboard or drum pad
(
MIDIdef.noteOn(\someKeyboard, { arg vel, note;
Synth("quick", [\freq, note.midicps, \amp, vel.linlin(0, 127, 0, 1)]);
});
)
// Create a pattern and play that from the keyboard
(
a = Pbind(
\instrument, "quick",
\degree, Pwhite(0, 10, 5),
\amp, Pwhite(0.05, 0.2),
\dur, 0.1
);
)
// test
a.play;
// Trigger pattern from pad or keyboard
MIDIdef.noteOn(\quneo, {arg vel, note; a.play});

// OSC
(
OSCdef(
	key: \whatever,
	func: {arg ... args; args.postln},
	path: '/stuff')
)

// Use this on the machine sending messages
~destination = NetAddr("127.0.0.1", 57120); // use correct IP address of destination computer
~destination.sendMsg("/stuff", "heelloooo");

(
// Record Output
s.record;
{Saw.ar(LFNoise0.kr([2, 3]).range(100, 2000), LFPulse.kr([4, 5]) * 0.1)}.play;
s.stopRecording;
s.makeWindow;  //Optional GUI
)