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
