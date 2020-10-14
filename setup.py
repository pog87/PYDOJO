from distutils.core import setup
setup(
    name='pydojo4',
    packages=['pydojo4'],
    version='4.0.3',
    description='A playful way to learn coding with Python',
    author='Alessandro Norfo, Davide Poggiali',
    author_email='sprintingkiwi@gmail.com, pog87@hotmail.it',
    url='https://github.com/pog87/PYDOJO',
    keywords=['game', 'development', 'learning', 'education'],
    classifiers=[],
    include_package_data=True,
    package_data={'pydojo4': ['turtle.png', 'pensurface.png']},
    install_requires=['pygame']
)
