I implemented the solution in `blockProcessor.py`. I made it in python because I'm more familiar with it but I don't mind learning a new language.

To run the solution just do:

```
python3 blockProcessor.py
```

It will run the examples given in the README file with some comments for clarification.

I added some thread locks for concurrency. Those are commented in the code for a better insight on why and where I put them. I also took an implementation decision for the case when the processed block has a different index than the received block. 