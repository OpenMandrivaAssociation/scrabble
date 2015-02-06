%define	version	1.5
%define release	7

Summary:	Text Mode Scrabble Word Game
Name:		scrabble
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		Games/Boards
URL:		http://packages.qa.debian.org/s/scrabble.html
Source:		%{name}-%{version}.tar.bz2
Patch0:		scrabble-1.5-hidden-config.patch.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl
BuildArch:	noarch

%description
Scrabble is a hybrid of crossword mentality, positional strategy, and a
true test of your language mastery. You start with a board that serves
for the placement for letter tiles. On the board there are specific
squares that when used can add to your score dramatically. These
premium squares can double or triple letter values. Some of these
squares can even double or triple your word scores! You must position
yourself to grab the squares and block your opponent from spelling
out a "killer" word.

This package is not for beginners as the display does not include
letter values or a description of what the symbols on the board
represent. You must be familiar with the game of Scrabble before
trying to play this version.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .hidden

%build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesbindir}/*
%{_datadir}/dict/*
%{_mandir}/man6/*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5-6mdv2010.0
+ Revision: 433627
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-5mdv2009.0
+ Revision: 260570
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-4mdv2009.0
+ Revision: 252182
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.5-2mdv2008.1
+ Revision: 127081
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import scrabble


* Wed Feb 09 2005 Abel Cheung <deaddog@mandrake.org> 1.5-2mdk
- Change game history file to .scrabble-games

* Mon Aug 23 2004 Abel Cheung <deaddog@mandrake.org> 1.5-1mdk
- First Mandrake package, imported from Debian package
