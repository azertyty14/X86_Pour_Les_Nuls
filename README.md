# X86 Pour Les Nuls

Le but est de pouvoir simuler les instructions assembleur X86 en python pour pouvoir facilement suivre la valeur des differents registres.

# Utilisation :

Pour executer les instructions d'un fichiers :
```bash
python3 ./main -f [FILE]
```
Par exemple pour run l'exemple de cours :
```bash
python3 ./main -f x86/exemple_cours.txt
```
Si vous voulez un mode pas à pas :
```bash
python3 ./main -i -f [FILE]
```

### TODO

- Ajouter les flags
- Ajouter les comparaisons et les jmp conditionnels
- Ajouter les opérations manquante
- Ajouter des arguments
- Mieux afficher les etats