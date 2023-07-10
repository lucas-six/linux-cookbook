# Join Files

## Recipes

Say we have a large file that has been split into multiple parts, and we want
to join them back together.
If the files were named: *movie.mp4.001*, *movie.mp4.002* ... *movie.mp4.099*.

```bash
cat movie.mp4.0* > movie.mp4
```
