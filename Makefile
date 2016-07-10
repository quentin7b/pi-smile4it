.PHONY: deploy, clean

deploy:
	rsync -a --exclude=.git ./ pi@192.168.0.17:~/Documents/App/pi-smile4it

clean:
	rm -rf */*.jpeg
