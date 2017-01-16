# http://world.std.com/~reinhold/dicewarefaq.html

if ! conda info --envs | grep diceware; then
conda create --name diceware python=3
fi
source activate diceware
python3 diceware.py --file diceware.wordlist.asc
source deactivate
