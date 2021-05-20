# CWAInfo Server

Dieser Teil des Projekts läuft auf dem zentralen Server und sammelt Informationen über alle Pi's.

## Installation

1. Klone diesen Teil der Repository auf den Server
1. Setze eine PostgreSQL DB und Apache mit PHP und Composer auf dem Server auf
1. Installiere die Dependencies mit `composer install`
1. Kopiere `.env.example` zu `.env` und passe die Datei an
1. Lasse die Migrations laufen mit `php artisan migrate`
