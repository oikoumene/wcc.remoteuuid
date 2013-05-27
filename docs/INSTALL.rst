wcc.remoteuuid Installation
---------------------------

To install wcc.remoteuuid using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``wcc.remoteuuid`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        wcc.remoteuuid

* Re-run buildout, e.g. with:

    $ ./bin/buildout

