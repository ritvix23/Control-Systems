from scipy import signal
import matplotlib.pyplot as plt

s = signal.lti([1], [1, 1, 3])
w, mag, phase = signal.bode(s)
plt.figure()
plt.semilogx(w, mag)  
plt.xlabel('frequency in radians')
plt.ylabel('gain in dB')  # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)
plt.xlabel('frequency in radians')
plt.ylabel('phase in degrees')  
plt.show()
