from dictionary import p_i, p_c, p_w, p_o_ixc , p_ts_cxw, p_r_oxts
print ('==================== Monte Carlo Inference of Bayesian Network =========================')
print ('Reference Values: ')
print ('\n   P(I)           = ' + str(p_i) + '\n   P(C)           = ' + str(p_c) + '\n   P(W)           = ' + str(p_w) + '\n   P(O  | I, C)   = ' + str(p_o_ixc) + '\n   P(TS | C, W)   = ' + str(p_ts_cxw) + '\n   P(R  | O, TS)  = ' + str(p_r_oxts))

print('\n\nFormula: \n   P(I ^ C ^ O ^ W ^ TS ^ R) = P(I)P(C)P(W)P(O|I,C)P(TS|C,W)P(R|O,TS)')
result = p_i * p_c * p_w * p_o_ixc * p_ts_cxw * p_r_oxts
print ('\n\nResult: \n   ' + str(result) + '\n\n')

