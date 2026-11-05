# sse-cursor-ledger

## Français

Rejouer les fragments SSE et les curseurs de reconnexion sans inventer des événements.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m sse_cursor_ledger examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Rejoue le cadrage SSE WHATWG, y compris décodage UTF-8 fragmenté, CR/LF, données multilignes et curseur Last-Event-ID entre connexions. Complète route-response-canary : ici le sujet est la reprise, pas la validation de fin de réponse.

### Limites

Captures fournies, sans navigateur ni serveur réel. Identifiants opaques : aucun trou numérique inféré ; réutilisation d’identifiant autorisée par le protocole, changement de contenu seulement signalé. UTF-8 invalide refusé.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Replay SSE chunks and reconnect cursors without inventing events.

Synthetic data; no network access or secret required.

```sh
python -m sse_cursor_ledger examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Replays WHATWG SSE framing including split UTF-8, CR/LF, multiline data and Last-Event-ID across connections. Complements route-response-canary: this focuses on resumption rather than response completion.

### Limits

Supplied captures, no actual browser or server. Opaque IDs: no inferred numeric gaps; the protocol permits ID reuse, so changed content is diagnostic only. Invalid UTF-8 is rejected.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Reproducir fragmentos SSE y cursores de reconexión sin inventar eventos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m sse_cursor_ledger examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Reproduce el encuadre SSE WHATWG: UTF-8 fragmentado, CR/LF, datos multilínea y Last-Event-ID entre conexiones. Complementa route-response-canary: trata reanudación, no finalización de respuesta.

### Límites

Capturas suministradas, sin navegador ni servidor real. IDs opacos: no se infieren huecos numéricos; reutilización permitida, cambio de contenido solo diagnóstico. UTF-8 inválido rechazado.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://html.spec.whatwg.org/multipage/server-sent-events.html

FR — alpha.2 signale aussi une ligne data finale non terminée comme jetée à EOF, sans émission ni progression du curseur. Les délais retry lus sont bornés à12 chiffres dans ce diagnostic.

EN — alpha.2 also reports a final unterminated data line discarded at EOF, without dispatch or cursor advancement. Parsed retry values are bounded to12 digits in this diagnostic.

ES — alpha.2 también indica una línea data final sin terminar descartada en EOF, sin emisión o avance de cursor. Valores retry analizados se limitan a12 dígitos en este diagnóstico.


## 2026-11-05 — FR / EN / ES

FR : Le rapport distingue désormais livraison répétée de même id/même contenu et même id/contenu différent. Tous les événements sont conservés : id SSE opaque ne garantit pas unicité métier ; le type n’est pas comparé dans ce diagnostic de contenu.

EN: Report now distinguishes repeated same-id/same-payload delivery from same-id/changed-payload replay. Every event is retained: opaque SSE IDs do not guarantee business uniqueness; event type is not compared in this payload diagnostic.

ES: El informe distingue entrega repetida con mismo id/contenido y mismo id/contenido cambiado. Conserva eventos: id SSE opaco no garantiza unicidad de negocio; este diagnóstico no compara tipo de evento.
