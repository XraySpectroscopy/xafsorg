# Makefile for Sphinx documentation
#


SPHINXBUILD = sphinx-build
BUILDDIR    = _build
SPHINXOPTS  = -d $(BUILDDIR)/doctrees .

.PHONY: html clean

html:
	$(SPHINXBUILD) -b html $(SPHINXOPTS) $(BUILDDIR)/html

clean:
	-rm -rf $(BUILDDIR)/*
