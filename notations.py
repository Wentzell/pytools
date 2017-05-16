# This module allows you to move from one mixed notation of the vertex into another stepping through an intermediate translation to the purely fermionic notation
# Here the notation implemented:
# PH, XPH, PP 
# PH, XPH, PP (shifted in order to get the 'vertex structure' in the middle 

#------------Imports---------------------

from mymath import *

#-------- Initialize the two dictionaries ------------------

toferm ={ };
fromferm ={ };

#-------- Purely fermionic-> Identity-------------------------

toferm['FERM'] = lambda (w1_in,w2_in,w1_out):(w1_in,w2_in,w1_out)

fromferm['FERM'] = lambda (w1_in,w2_in,w1_out):(w1_in,w2_in,w1_out)

#-------- TRIQS -------------------------

toferm['TRIQS'] = lambda (w1_in, w2_in, w1_out):(w1_in, w1_out, w2_in)

fromferm['TRIQS'] = lambda (w1_in, w1_out, w2_in):(w1_in, w2_in, w1_out)

#-------- POMEROL -------------------------

toferm['POM'] = lambda (w1_out, w2_out, w2_in):(w1_out + w2_out - w2_in, w2_in, w1_out)

fromferm['POM'] = lambda (w1_in, w2_in, w1_out):(w1_out, w1_in + w2_in - w1_out, w2_in)

#-------- PP ( Vertex paper, only outgoing legs flipped ) -------------------------

toferm['PP'] = lambda (W, w_in, w_out):(w_in, W - w_in, w_out)

fromferm['PP'] = lambda (w1_in, w2_in, w1_out):(w1_in + w2_in, w1_in, w1_out)

#-------- PH ( Vertex paper ) -------------------------

toferm['PH'] = lambda (W, w_in, w_out):(w_in, w_out + W, w_in + W)

fromferm['PH'] = lambda (w1_in, w2_in, w1_out):(w1_out - w1_in, w1_in, w2_in - (w1_out - w1_in))

#-------- XPH ( Vertex paper ) -------------------------

toferm['XPH'] = lambda (W, w_in, w_out):(w_in, w_out + W, w_out)

fromferm['XPH'] = lambda (w1_in, w2_in, w1_out):(w2_in - w1_out, w1_in, w2_in - (w2_in - w1_out))

# ===== ADJUST 

# #-------- PP shifted-------------------------

# toferm['PP_shift'] = lambda (i,j,k):(j+ceil_div2(i),-j+floor_div2(i)-1,k+ceil_div2(i))

# fromferm['PP_shift'] = lambda (i,j,k):(i+j+1,i-ceil_div2(i+j+1),k-ceil_div2(i+j+1))


# #-------- PH shifted-------------------------

# toferm['PH_shift'] = lambda (i,j,k):(j-floor_div2(i),k+ceil_div2(i),j+ceil_div2(i))

# fromferm['PH_shift'] = lambda (i,j,k):(k-i,i+floor_div2(k-i),j-ceil_div2(k-i))


# #-------- XPH shifted-------------------------

# toferm['XPH_shift'] = lambda (i,j,k):(j-floor_div2(i),k+ceil_div2(i), k-floor_div2(i))

# fromferm['XPH_shift'] = lambda (i,j,k):(j-k,i+floor_div2(j-k),j-ceil_div2(j-k))


#--------------- TRANSLATION FUNCTION -----------------------------

def translate( notout, notin ):
    return lambda (i,j,k): fromferm[notout]((toferm[notin]((i,j,k))))


#------------------- Define useful objects--------------------------

