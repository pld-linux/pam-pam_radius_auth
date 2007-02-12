%define 	modulename	pam_radius
Summary:	PAM module - authenticate using RADIUS server
Summary(pl.UTF-8):   Moduł PAM pozwalający na użycie serwera RADIUS do uwierzytelniania
Name:		pam-%{modulename}_auth
Version:	1.3.16
Release:	1
License:	GPL
Group:		Networking
Source0:	ftp://ftp.freeradius.org/pub/radius/%{modulename}-%{version}.tar
# Source0-md5:	633d57c7035671fe7655158e37633db7
URL:		http://www.freeradius.org/pam_radius_auth/
BuildRequires:	pam-devel > 0.77.3-2
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the PAM to RADIUS authentication module. It allows any
PAM-capable machine to become a RADIUS client for authentication and
accounting requests. You will need a RADIUS server to perform the
actual authentication.

%description -l pl.UTF-8
To jest moduł do PAM służący uwierzytelnianiu użytkowników względem
serwera RADIUS. Pozwala każdej maszynie korzystającej z PAM zostać
klientem usługi RADIUS w celach uwierzytelniania użytkowników oraz
zbierania statystyk logowań (accounting). Do dokonania samego
uwierzytelnienia niezbędny jest serwer RADIUS.

%prep
%setup -q -n %{modulename}-%{version}

sed -i -e 's/ld -Bshareable/$(CC) -shared/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}/security

install pam_radius_auth.so $RPM_BUILD_ROOT/%{_lib}/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO USAGE INSTALL pam_radius_auth.conf
%attr(755,root,root) /%{_lib}/security/pam_radius_auth.so
