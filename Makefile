all: all-modules

all-modules:
	cd modules/ && $(MAKE)
