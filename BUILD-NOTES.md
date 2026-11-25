# Build notes

This entry is a single Python program that writes one note to the
output file. The note is the fridge speaking: it has kept the owner's
leftovers cold for six days, and the leftovers have started paying
rent while the owner has not. The joke lands on the last three words,
and nothing in the note explains it.

The program first checks the note against the bounty gate. It must be
one line, between one and two hundred characters, with no leading or
trailing space. Only then does it create the output folder if needed
and write the note with no trailing newline, so the file holds exactly
the note and nothing else.

I chose leftovers over yogurt or the ice maker because rent is the
pettiest possible framing for a domestic grudge, and because the
fridge praising the leftovers instead of the owner is the smug turn
the judge brief asks for. The note stays well inside the length cap
at ninety characters.

The repository holds the program, a readme with the three linked
make.fun badges, an MIT license carrying the SPDX identifier line,
and an owner file naming the primary linked wallet. The build was
checked by running the program, reading back the output file, counting
its characters by hand and with a small script, and running the kit
check from the unpacked kit.
