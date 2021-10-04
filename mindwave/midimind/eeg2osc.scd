s.boot;
s.stop;

Quarks.gui;
Quarks.save("~/Music/sc/quarks.txt");
Quarks.clear;

{RLPF.ar(Dust.ar([12, 15]), LFNoise1.ar([0.3, 0.2]).range(100, 3000), 0.02)}.play;

thisProcess.openUDPPort(4560);         // open the  UDP port
n = NetAddr.("192.168.1.100", 4560);    // create the NetAddr
n.free;


// create the OSC listener
(o = OSCdef(  \eeg,
	{ |msg, time, source|
		var data = msg.copyToEnd(1);
		~time = data[0];
		~signal = data[1];
		~atn = data[2];
		~med = data[3];
		~delta = data[4];
		~theta = data[5];
		~l_alpha = data[6];
		~h_alpha = data[7];
		~l_beta = data[8];
		~h_beta = data[9];
		~l_gamma = data[10];
		~m_gamma = data[11];

		msg.postln;
	},
	'/eeg' );
)
o.free;


"attention: " + ~atn.postlnw
"meditation: " + ~med.postln;

Ndef( \sines, { SinOsc.ar( \freq.kr( 300, 0.1 ), 0, \amp.kr(0.1, 0.1) ) } );
Ndef( \sines ).play;

f = { SinOsc.ar(440 + 200.rand, 0, 0.2) };
x = f.play;
x.free;

SCLOrkSynths.gui;
SCLOrkSynths.directory
SCLOrkSynths.load
SCLOrkSynths.synthDictionary

SynthDefPool.gui;

