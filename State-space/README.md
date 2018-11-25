Min state-space:

Min formule = 1 + bk

1 = want je moet altijd de rode auto verschuiven
bk = aantal auto's/vrachtwagens die de rode auto blokkeren


Max State-space:

Max formule: (bg-1) ^ (ka) * (bg-2) ^ (vr) = mx
bg = bord grootte, aantal vakjes in een rij
ka = aantal kleine auto's
vr = aantal vrachtwagens
mx = maximale state-space


Game_1:
- 6 auto's (5 zetten)
- 3 vrachtwagens (4 zetten)

> Min formule: 1 + 1 = 2
> Max formule: 5^6 * 4^3 = 10^6 (1000000)

Game_2:

- 12 auto's (5 zetten)
- 1 vrachtwagen (4 zetten)

> Min formule: 1 + 2 = 3
> Max formule: 5^12 * 4^1 = 976562500

- 6 2(zelfde rij) vlaksauto's(3 zetten)
- 1 3 vlaksauto(4 zetten)
- 5 2(niet zelfde rij) vlaksauto's (5 zetten)

> 3^6 * 4^1 * 5^5 = 9112500 = 9*10^6

Game_3:

- 12 auto's (5 zetten)
- 1 vrachtwagen (4 zetten)

> Min formule: 1 + 3 = 4
> Max formule: 5^12 * 4^1 = 976562500

- 1 2/3(zelfde rij) vlaksauto (2 zetten)
- 1 3/2 (zelfde rij) vlaksauto (2 zetten)
- 6 2 (zelfde rij) 2 vlaksauto's (3 zetten)
- 4 2 vlaksautos (5 zetten)

> 2^1 * 2^1 * 3^6 * 5^4 = 1822500 = 2*10^6

Game_4:

- 12 auto's (8 zetten)
- 10 vrachtwagens (7 zetten)

> Min formule: 1 + 2 = 3
> Max formule: 8^12 * 7^10 = 1.94115513e19

Game_5:

- 18 auto's (8 zetten)
- 6 vrachtwagens (7 zetten)

> Min formule: 1 + 1 = 2
> Max formule: 8^18 * 7^6 = 2.11937591e21

Game_6:

- 18 auto's (8 zetten)
- 8 vrachtwagens (7 zetten)

> Min formule: 1 + 2 = 3
> Max formule: 8^18 * 7^8 = 1.038494225e23

Game_7:

- 28 auto's (11 zetten)
- 16 vrachtwagens (10 zetten)

> Min formule: 1 + 2 = 4
> Max formule: 11^12 * 10^16 = 3.138428377e28
