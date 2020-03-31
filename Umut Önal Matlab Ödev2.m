%SORU1

rl = (1:1:100);
v = (120);
rs = (50);
Pl = rl*rs
Amper = rl/v

%%
%SORU2
input=('karbon yüzdesi giriniz:');
f = sym('&lambda;');
int(f) = (0.00012097);
sym('(#14)/#100');
%%
%SORU3
g = ('(#99)*unit::s)*unit::m');
sym('&theta;') = ('0 to &pi;/2 , incremendent by 0.05');
sym('&upsi;[#0]') = ('50((#m)/#s) and 100((#m)/#s)');