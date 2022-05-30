# Exercise 4:(LAB 4 – OOP)
# In this lab you have one person in a band that wants to play some instruments...
# Create one function and name it play_instrument( ) which will receive an instance of an instrument and will print its play () method.
import drums
import synth


def play_instrument(instrument):
    return instrument.play()

drums = drums.Drums()
play_instrument(drums)

synth = synth.Synth()
play_instrument(synth)




    