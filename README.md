brew# Dynon Serial Data Decoder

This library is a decoder of [Dynon Skyview (HDX) Serial Data Structure](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.dynonavionics.com/includes/guides/SkyView_System_Installation_Guide-Rev_AF-v15_4.pdf)
and the older Dynon D100/D120/D180 series data structures.

## How to install
```
python setup.py
```

## How to use
```
python3 dyndecode.py [infile] -f [outfile] - where infile can also be stdin & outfile stdout.
e.g. cat data.txt | python3 dyndecode.py

Data is CRC checked, invalid lines are silently skipped.
```

## Known Issues
```
Still a work in progress, Skyview ems & system not working correctly yet with test data. D1x0 EMS data is converted to degC & litres. - need to implement a command line option for data conversion. D1x0 EFIS not fully decoded.
```

## References

- [Dynon Skyview System Installation Guide](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.dynonavionics.com/includes/guides/SkyView_System_Installation_Guide-Rev_AF-v15_4.pdf)

Author : Taylor Hoshino & Jon Lidgard
